#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """Calculate the start and end index for pagination."""
    start = (page - 1) * page_size
    end = start + page_size

    return start, end
