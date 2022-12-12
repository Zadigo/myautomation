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
