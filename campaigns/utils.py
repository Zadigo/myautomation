import json
import pathlib
import random
from functools import lru_cache, wraps

from django.conf import settings
from django.utils.crypto import get_random_string


def split_values(value, separator=','):
    return value.split(separator)


def upload_file_to(instance, name):
    new_name = f'{get_random_string(20)}.csv'
    return f'campaigns/{instance.id}/{new_name}'


class LogicalMapFormatter:
    # [{"tag": "div", "attrs": {"name": "id", "operator": "=", "value": "google"}}]
    def __init__(self, value=None):
        self.tag = None
        self._attrs = {}
        self.attrs = {}

        if value is not None:
            self.tag = value['tag']
            self._attrs = value['attrs']

            if self._attrs['operator'] == '=':
                self.attrs = {self._attrs['name']: self._attrs['value']}

    @classmethod
    def build(cls, logical_maps):
        """Build multiple maps 
        at once"""
        result = []
        for item in logical_maps:
            result.append(cls(item))
        return item
