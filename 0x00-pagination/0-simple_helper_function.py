#!/usr/bin/ env python3
"""Index xrange"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a page and page size.

    :param page: The page number (1-indexed)
    :param page_size: The number of items per page
    :return: A tuple containing the start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
