#!/usr/bin/env python3
"""
100-lfu_cache.py
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache
    """
    def put(self, key, value):
        """
        Puts item to cache.
        """
        if not key or not value:
            return

        cache_data = self.cache_data

        if len(cache_data) == self.MAX_ITEMS and key not in cache_data:
            discard = min(cache_data, key=lambda k: cache_data[k]["score"])
            del cache_data[discard]

            print(f"DISCARD: {discard}")

        if key not in cache_data:
            cache_data[key] = {"value": value, "score": 1}
        else:
            cache_data[key]["value"] = value
            cache_data[key]["score"] += 1

    def get(self, key):
        """
        Gets item from cache.
        """
        if key in self.cache_data:
            self.cache_data[key]["score"] += 1
            return self.cache_data[key]["value"]

    def print_cache(self):
        """
        Prints the cache.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data[key]["value"]))
