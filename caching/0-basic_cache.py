#!/usr/bin/python3
"""
BasicCache class
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """
    def put(self, key, item):
        """
        Save item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
