#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
        """return a dictionary with stats"""
        assert index < len(self.__indexed_dataset) and index >= 0

        keys = list(self.__indexed_dataset.keys())
        if index in keys:
            start_slice = keys.index(index)
        else:
            start_slice = index
        keys = keys[start_slice: start_slice + page_size]
        data = [self.__indexed_dataset[i] for i in keys]
        hyper_index = {
            "index": index, "next_index": keys[0] + page_size,
            "page_size": page_size, "data": data
        }
        print("KEYS: ", keys)
        return hyper_index
