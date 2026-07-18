"""Volatile, per-browser-session credential storage. Never serialize values."""

from threading import RLock


class VolatileCredentialStore:
    def __init__(self):
        self._keys = {}
        self._lock = RLock()

    def set_openai_key(self, session_key, api_key):
        with self._lock:
            self._keys[session_key] = api_key

    def has_openai_key(self, session_key):
        with self._lock:
            return bool(self._keys.get(session_key))

    def get_openai_key(self, session_key):
        with self._lock:
            return self._keys.get(session_key)

    def clear_openai_key(self, session_key):
        with self._lock:
            self._keys.pop(session_key, None)


credential_store = VolatileCredentialStore()
