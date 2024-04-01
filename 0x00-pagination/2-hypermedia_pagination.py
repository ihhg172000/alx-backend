#!/usr/bin/env python3
"""
1-simple_pagination.py
"""
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns start and end indexes for pagination parameters.
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return (start_idx, end_idx)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Paginates the dataset and returns the appropriate page of the dataset.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_idx: end_idx]

    def get_hyper(self, p: int = 1, s: int = 10) -> Dict:
        """
        Paginates the dataset and returns the appropriate page of the dataset.
        """
        data = self.get_page(p, s)
        page_size = len(data)
        total_pages = math.ceil(len(self.dataset()) / s)
        prev_page = p - 1 if p > 1 else None
        next_page = p + 1 if p < total_pages else None

        return {
            "page_size": page_size,
            "page": p,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
