from campaigns.utils import upload_file_to
from campaigns.validators import (validate_csv_file, validate_proxies,
                                  validate_urls)
from django.db import models
from django.utils.functional import cached_property


class Campaign(models.Model):
    name = models.CharField(
        max_length=100
    )
    urls = models.CharField(
        max_length=1000,
        validators=[validate_urls]
    )
    results_per_search = models.PositiveIntegerField(
        default=100
    )
    csv_file = models.FileField(
        upload_to=upload_file_to,
        validators=[validate_csv_file],
        help_text="A file used to parse a list of urls. Should have 'website' header",
        blank=True,
        null=True
    )
    retries = models.PositiveIntegerField(
        default=0
    )
    proxies = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        help_text='List of proxies to use for the request',
        validators=[validate_proxies]
    )
    section_to_parse = models.CharField(
        max_length=100,
        help_text='Only parse a specific section of the given HTML page',
        blank=True,
        null=True
    )
    parse_all_tables = models.BooleanField(
        default=False
    )
    parse_all_text = models.BooleanField(
        default=False
    )
    runned = models.BooleanField(
        default=False,
        help_text='True if the campaigned was runned at least once'
    )
    paused = models.BooleanField(
        default=False,
    )
    archived = models.BooleanField(
        default=False
    )
    draft = models.BooleanField(
        default=True
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @cached_property
    def campaign_urls(self):
        if self.urls is None:
            return []
        return self.urls.split(',')
