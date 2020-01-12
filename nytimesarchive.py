#!/usr/bin/python3
import requests
"""
About:
Python wrapper for the New York Times Archive API 
https://developer.nytimes.com/article_search_v2.json
"""

class APIKeyException(Exception):
    def __init__(self, message): self.message = message 

class InvalidQueryException(Exception):
    def __init__(self, message): self.message = message 

class ArchiveAPI(object):
    def __init__(self, key=None):
        """
        Initializes the ArchiveAPI class. Raises an exception if no API key is given.
        :param key: New York Times API Key
        """
        self.key = key
        self.root = 'http://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}' 
        if not self.key:
            nyt_dev_page = 'http://developer.nytimes.com/docs/reference/keys'
            exception_str = 'Warning: API Key required. Please visit {}'
            raise NoAPIKeyException(exception_str.format(nyt_dev_page))

    def query(self, year=None, month=None, key=None,):
        """
        Calls the archive API and returns the results as a dictionary.
        :param key: Defaults to the API key used to initialize the ArchiveAPI class.
        """
        if not key: key = self.key
        exception_str = 'Invalid query: See https://developer.nytimes.com/docs/archive-product/1/overview'
        if not (0 < month < 13):
            raise InvalidQueryException('Month must be between 1 and 12, inclusive.\n{}'.format(exception_str)) 
        if (year, month) < (1851, 9):
            raise InvalidQueryException('Articles are only available from September 1851 and later.\n{}'.format(exception_str))
        url = self.root.format(year, month, key)
        r = requests.get(url)
        return r.json()
