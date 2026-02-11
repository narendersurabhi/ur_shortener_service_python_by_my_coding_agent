import threading
import logging
from datetime import datetime
from typing import Optional, Dict

logger = logging.getLogger(__name__)

# Small base62 alphabet for compact keys
_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
_BASE = len(_ALPHABET)


def _encode(num: int) -> str:
    if num == 0:
        return _ALPHABET[0]
    chars = []
    while num > 0:
        num, rem = divmod(num, _BASE)
        chars.append(_ALPHABET[rem])
    return "".join(reversed(chars))


class InMemoryStorage:
    """Thread-safe in-memory storage for URL -> key mappings.

    Features:
    - Generate short keys using an incrementing counter encoded in base62.
    - Support optional custom keys (validated to contain only alphabet chars).
    - Deduplicate: if the same long URL was already shortened, return the existing key.
    - Minimal metadata stored (created_at).
    """

    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._counter = 1
        self._store: Dict[str, Dict] = {}  # key -> {url, created_at}
        self._reverse: Dict[str, str] = {}  # url -> key

    def create(self, url: str, custom_key: Optional[str] = None) -> str:
        """Store url and return a short key. If url already exists, return existing key.

        If custom_key is provided, it must be composed of allowed alphabet characters
        and must not already be in use.
        """
        if not url:
            raise ValueError("url must be a non-empty string")

        with self._lock:
            # Return existing key for same URL
            existing = self._reverse.get(url)
            if existing:
                logger.debug("URL already shortened: %s -> %s", url, existing)
                return existing

            if custom_key:
                if any(c not in _ALPHABET for c in custom_key):
                    raise ValueError("custom_key contains invalid characters")
                if custom_key in self._store:
                    raise KeyError("custom_key already in use")
                key = custom_key
            else:
                # allocate next available key
                key = _encode(self._counter)
                # ensure no collision (unlikely) by incrementing
                while key in self._store:
                    self._counter += 1
                    key = _encode(self._counter)
                self._counter += 1

            now = datetime.utcnow().isoformat() + "Z"
            self._store[key] = {"url": url, "created_at": now}
            self._reverse[url] = key
            logger.info("Created short url: %s -> %s", key, url)
            return key

    def get(self, key: str) -> Optional[str]:
        """Retrieve the original URL for a given short key, or None if not found."""
        if not key:
            return None
        with self._lock:
            item = self._store.get(key)
            if item:
                logger.debug("Resolved key %s -> %s", key, item["url"])
                return item["url"]
            logger.debug("Key not found: %s", key)
            return None

    def exists(self, key: str) -> bool:
        with self._lock:
            return key in self._store

    def stats(self) -> Dict[str, int]:
        with self._lock:
            return {"count": len(self._store)}


# module-level singleton for convenient use in the app
_storage = InMemoryStorage()


def get_storage() -> InMemoryStorage:
    return _storage
