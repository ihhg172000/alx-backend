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

        cache_is_full = len(cache_data) == self.MAX_ITEMS
        key_is_not_in_cache = key not in cache_data.keys()

        if cache_is_full and key_is_not_in_cache:
            keys = list(cache_data.keys())
            discard = keys[0]

            for k in keys:
                if cache_data[k]["score"] < cache_data[discard]["score"]:
                    discard = k

            del cache_data[discard]

            print(f"DISCARD: {discard}")

        if key_is_not_in_cache:
            cache_data[key] = {"value": value, "score": 1}
        else:
            cache_data[key]["value"] = value
            cache_data[key]["score"] += 1

    def get(self, key):
        """
        Gets item from cache.
        """
        if key:
            cache_data = self.cache_data

            try:
                cache_data[key]["score"] += 1
                return cache_data[key]["value"]
            except (KeyError):
                pass

    def print_cache(self):
        """
        Prints the cache.
        """
        cache_data = self.cache_data

        print("Current cache:")
        for key in sorted(cache_data.keys()):
            print("{}: {}".format(key, cache_data.get(key).get("value")))
