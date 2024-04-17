#!/usr/bin/python3
"""
BasicCache class
"""

from typing import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    BasicCache class LRU
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.key_access = []

    def put(self, key, item):
        """
        Save item
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key not in self.key_access:
            self.key_access.append(key)
        else:
            self.key_access.append(self.key_access.pop
                                   (self.key_access.index(key)))
        if len(self.key_access) > BaseCaching.MAX_ITEMS:
            discard = self.key_access.pop(-2)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

    def get(self, key):
        """
        Get item
        """
        if key is not None and key in self.cache_data:
            self.key_access.remove(key)
            self.key_access.append(key)
            return self.cache_data[key]
        return None
