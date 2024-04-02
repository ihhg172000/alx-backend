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
        self.cache_stack = []

    def put(self, key, value):
        """
        Puts item to cache.
        """
        if not key or not value:
            return

        cache_is_full = len(self.cache_data) == self.MAX_ITEMS
        key_is_not_in_cache = key not in self.cache_data.keys()

        if cache_is_full and key_is_not_in_cache:
            discard = self.cache_stack.pop()
            del self.cache_data[discard]

            print(f"DISCARD: {discard}")

        self.cache_data[key] = value

        try:
            self.cache_stack.remove(key)
        except (ValueError):
            pass

        self.cache_stack.append(key)

    def get(self, key):
        """
        Gets item from cache.
        """
        if key:
            try:
                return self.cache_data[key]
            except (KeyError):
                pass
