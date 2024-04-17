#!/usr/bin/python3
"""
BasicCache class
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    BasicCache class
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Save item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print(f'DISCARD: {discard}')

    def get(self, key):
        """
        Get item
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
