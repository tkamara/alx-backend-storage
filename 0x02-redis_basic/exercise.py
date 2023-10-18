#!/usr/bin/env python3
"""writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """creating Cache class"""
    def __init__(self):
        """initializing"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ 
        generate a random key (e.g. using uuid)
        store the input data in Redis using the random key
        and return the key
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return str(rand_key)

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        take a key string argument and an optional Callable argument named fn
        This callable will be used to convert the data back to the desired format
        """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: str) -> str:
        """
        convert to UTF-8 decoded
        """
        return data.decode("utf-8")

    def get_int(self, data: str) -> int:
        """
        convert to int
        """
        return int(data)


