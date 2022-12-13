from campaigns.utils import split_values
from django.core import validators
from urllib.parse import urlparse
from django.core.exceptions import ValidationError

# List of domains that should not be 
# scrapped otherwise the website might
# be blocked
DOMAIN_BLOCKLIST = [
    'facebook.com',
    'linkedin.com'
]

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


def validate_url(value):
    instance = urlparse(value)
    if instance.netloc in DOMAIN_BLOCKLIST:
        raise ValidationError(f'The domain {value} is not valid')
