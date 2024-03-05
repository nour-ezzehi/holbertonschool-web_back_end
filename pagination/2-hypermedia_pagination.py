#!/usr/bin/env python3
""" Hypermedia pagination """

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Calculates both the start and end index for pagination
    """
    start = (page - 1) * page_size
    end = start + page_size

    return start, end


class Server:
    """
    paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Retrieve a specific page
        """
        assert isinstance(
            page, int) and isinstance(
            page_size, int), "page and page_size must be integers."
        assert page > 0 and page_size > 0, \
            "page and page_size must be greater than 0."

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Retrieve pagination information in a dictionary
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
