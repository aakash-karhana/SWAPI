"""
Creates a log file for user to see from where this data comes from
"""

import logging


def logger(func):
    def wrapper(url):
        try:
            logging.info(f"Fetching the data from url - {url}")
            bar = func(url)
            logging.info(f"success code - {bar.status_code}")
        except Exception:
            logging.error(f"There are some errors while fetching the data from url - {url}")

        return bar
    return wrapper
