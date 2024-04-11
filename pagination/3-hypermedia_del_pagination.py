#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        return a dictionary
        """
        assert 0 <= index < len(self.dataset())

        dataset_length = len(self.dataset())
        indexed_dataset = self.indexed_dataset()
        page_data = []

        while len(page_data) < page_size and index < dataset_length:
            if index in indexed_dataset:
                page_data.append(indexed_dataset[index])
            index += 1

        next_index = index if index < dataset_length else None
        return {
            'index': index - len(page_data),
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data
        }
