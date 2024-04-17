#!/usr/bin/python3
"""
BasicCache class
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.stack.remove(key)
        self.stack.append(key)
        self.cache_data[key] = item
        if len(self.stack) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Get item
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
