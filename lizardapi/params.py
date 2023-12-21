from typing import Any


class Query:
    def __init__(self, default: Any, ge: int = 0, le: int = 0, lt: int = 0):
        self._default = default


class Path:
    def __init__(self, default: Any, ge: int = 0, le: int = 0, lt: int = 0):
        self._default = default
