import json
import pathlib
import random
from functools import lru_cache

from django.conf import settings


def media_path(filename):
    def wrapper(func):
        def inner():
            media_root = pathlib.Path(settings.MEDIA_ROOT)
            with open(media_root.joinpath(filename), mode='r', encoding='utf-8') as f:
                data = json.load(f)
                return func(data)
        return inner
    return wrapper


def get_default_proxies():
    """Returns the list of default proxies to
    use for sending requests"""
    proxies = []
    media_root = pathlib.Path(settings.MEDIA_ROOT)
    with open(media_root.joinpath('proxies.json'), mode='r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            proxies.append(('https' if item['secured'] else 'http', item['host']))
    return proxies


@lru_cache(maxsize=5)
def get_proxies():
    """Returns the list of default proxies by
    caching them efficiently for better
    performance"""
    return list(get_default_proxies())


def get_random_proxies(k=10):
    """Returns a list of 10 randomly selected
    proxies"""
    proxies = list(get_proxies())
    random.shuffle(proxies)
    if k > len(proxies):
        k = len(proxies)
    return random.sample(proxies, k)


@media_path('user_agents.json')
def get_user_agents(data):
    for item in data:
        yield item


@media_path('headers.json')
def get_headers(data):
    for item in data:
        yield item


def get_random_header():
    headers = get_headers()
    random.shuffle(headers)
    return random.choice(headers)


@lru_cache(maxsize=100)
def get_settings_for_parsed_website(domain):
    if domain.startswith('http') or domain.startswith('https'):
        raise ValueError('Domain should not start with http or https')

    tried = []
    media_root = pathlib.Path(settings.MEDIA_ROOT)
    with open(media_root.joinpath('websites.json'), mode='r', encoding='utf-8') as f:
        valid_domain = {}
        data = json.load(f)
        for item in data:
            if domain in item['url']:
                valid_domain = item
                break
            else:
                tried.append(item)
        return valid_domain
