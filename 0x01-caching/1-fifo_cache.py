#!/usr/bin/env python3
"""
1-fifo_cache.py
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache
    """
    def __init__(self):
        """
        Init.
        """
        super().__init__()
        self._cache_queue = []

    def put(self, key, value):
        """
        Puts item to cache.
        """
        if not key or not value:
            return

        cache_data = self.cache_data

        if len(cache_data) == self.MAX_ITEMS and key not in cache_data:
            discard = self._cache_queue.pop(0)
            del cache_data[discard]

            print(f"DISCARD: {discard}")

        cache_data[key] = value

        if key in self._cache_queue:
            self._cache_queue.remove(key)

        self._cache_queue.append(key)

    def get(self, key):
        """
        Gets item from cache.
        """
        return self.cache_data.get(key)
