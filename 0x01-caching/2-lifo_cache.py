#!/usr/bin/env python3
"""2-lifo_cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last In First Out caching system"""
    def __init__(self):
        """Class constructor"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key and delete a value if necesary"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = list(self.cache_data.keys())[-2]
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

    def get(self, key):
        """ return the value in self.cache_data linked to key"""
        return self.cache_data.get(key)
