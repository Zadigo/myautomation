from campaigns.utils import split_values
from django.core import validators


def validate_csv_file(name):
    validator = validators.FileExtensionValidator(allowed_extensions=['csv'])
    validator(name)


def validate_proxies(value):
    items = split_values(value)
    for ip in items:
        validators.validate_ipv4_address(ip)


def validate_urls(value):
    validator = validators.URLValidator()
    items = split_values(value)
    for url in items:
        validator(url)
