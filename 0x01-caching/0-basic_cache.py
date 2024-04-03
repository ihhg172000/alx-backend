#!/usr/bin/env python3
"""
0-basic_cache.py
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BaseCaching
    """
    def put(self, key, value):
        """
        Puts item to cache.
        """
        if key and value:
            self.cache_data[key] = value

    def get(self, key):
        """
        Gets item from cache.
        """
        return self.cache_data.get(key)
