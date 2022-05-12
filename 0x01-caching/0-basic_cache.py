#!/usr/bin/env python3
"""0-basic_cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This class is a caching system"""
    def __init__(self):
        """Class constructor"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key)
