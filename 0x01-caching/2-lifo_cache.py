#!/usr/bin/env python3
"""
2-lifo_cache.py
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache
    """
    def __init__(self):
        """
        Init.
        """
        super().__init__()
        self._cache_stack = []

    def put(self, key, value):
        """
        Puts item to cache.
        """
        if not key or not value:
            return

        cache_data = self.cache_data

        if len(cache_data) == self.MAX_ITEMS and key not in cache_data:
            discard = self._cache_stack.pop()
            del cache_data[discard]

            print(f"DISCARD: {discard}")

        cache_data[key] = value

        if key in self._cache_stack:
            self._cache_stack.remove(key)

        self._cache_stack.append(key)

    def get(self, key):
        """
        Gets item from cache.
        """
        return self.cache_data.get(key)
