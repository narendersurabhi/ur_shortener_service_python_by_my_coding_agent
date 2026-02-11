from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from pydantic import BaseModel, AnyHttpUrl
import secrets
import logging
import json

# App and in-memory store
app = FastAPI()
_store = {}

# Structured logger
logger = logging.getLogger("url_shortener")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Request model
class ShortenRequest(BaseModel):
    url: AnyHttpUrl


def _log(action: str, **kwargs):
    entry = {"action": action, **kwargs}
    logger.info(json.dumps(entry))


@app.post("/shorten")
async def shorten(payload: ShortenRequest, request: Request):
    original = str(payload.url)
    # if already shortened, return existing code
    for code, val in _store.items():
        if val == original:
            short = f"{str(request.base_url).rstrip('/')}/{code}"
            _log("create_reuse", code=code, original=original, short_url=short)
            return JSONResponse(status_code=200, content={"code": code, "short_url": short})

    # generate short code
    code = secrets.token_urlsafe(6)
    code = code.replace("-", "_")[:8]
    _store[code] = original
    short = f"{str(request.base_url).rstrip('/')}/{code}"
    _log("create", code=code, original=original, short_url=short, client_ip=(request.client.host if request.client else None))
    return JSONResponse(status_code=201, content={"code": code, "short_url": short})


@app.get("/{code}")
async def follow(code: str, request: Request):
    original = _store.get(code)
    if not original:
        _log("miss", code=code, client_ip=(request.client.host if request.client else None))
        raise HTTPException(status_code=404, detail="Short URL not found")
    _log("redirect", code=code, original=original, client_ip=(request.client.host if request.client else None))
    return RedirectResponse(original)


@app.get("/health")
async def health():
    return {"status": "ok"}
