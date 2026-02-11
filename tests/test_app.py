import importlib
import urllib.parse
import pytest

from fastapi.testclient import TestClient

CANDIDATE_MODULES = ["app.main", "main", "app", "src.main"]


def get_app():
    for name in CANDIDATE_MODULES:
        try:
            mod = importlib.import_module(name)
        except Exception:
            continue
        # common patterns
        if hasattr(mod, "app"):
            return getattr(mod, "app")
        if hasattr(mod, "create_app"):
            return getattr(mod, "create_app")()
        if hasattr(mod, "application"):
            return getattr(mod, "application")
    pytest.skip("Could not find FastAPI/Flask app module. Tried: %s" % ",".join(CANDIDATE_MODULES))


def extract_short_path(data):
    # Try common keys
    for key in ("short_url", "short", "alias", "url", "id", "key"):
        if key in data:
            val = data[key]
            if not isinstance(val, str):
                continue
            parsed = urllib.parse.urlparse(val)
            if parsed.path and parsed.path != "":
                return parsed.path
            return "/" + val.lstrip("/")
    # fallback: if the response itself looks like a URL string
    if isinstance(data, str):
        parsed = urllib.parse.urlparse(data)
        if parsed.path:
            return parsed.path
    return None


def test_health():
    app = get_app()
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    try:
        data = r.json()
    except ValueError:
        pytest.fail("/health did not return JSON")
    assert "status" in data
    assert any(sub in str(data["status"]).lower() for sub in ("ok", "healthy", "up"))


def test_shorten_and_redirect():
    app = get_app()
    client = TestClient(app)
    original = "https://example.org/path?query=1"

    # create a short URL
    r = client.post("/shorten", json={"url": original})
    assert r.status_code in (200, 201), f"unexpected status {r.status_code}: {r.text}"
    data = r.json()

    short_path = extract_short_path(data)
    assert short_path, f"no short url/id found in response: {data}"

    # request the short url (no automatic redirects)
    r2 = client.get(short_path, allow_redirects=False)
    assert r2.status_code in (301, 302, 307, 308), f"expected redirect, got {r2.status_code}"
    assert r2.headers.get("location") == original
