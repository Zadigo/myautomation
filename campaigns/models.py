from campaigns.utils import upload_file_to
from campaigns.validators import (validate_csv_file, validate_proxies,
                                  validate_urls, validate_url)
from django.db import models
from django.utils.functional import cached_property
from campaigns.choices import WebRequests

# class Proxy(models.Model):
#     ip_address = models.IPAddressField()
#     secured = models.BooleanField(default=False)
#     risky = models.BooleanField(default=False)

#     def __str__(self):
#         return self.ip_address


class Action(models.Model):
    url = models.URLField(
        max_length=1000,
        validators=[validate_url]
    )
    web_request = models.CharField(
        max_length=100,
        choices=WebRequests.choices,
        default=WebRequests.GET
    )
    runned = models.BooleanField(default=False)
    created_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.url


class Campaign(models.Model):
    name = models.CharField(
        max_length=100
    )
    actions = models.ManyToManyField(Action, blank=True)
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
        help_text='List of proxies provided by the user for the request',
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

    class Meta:
        ordering = ['name', 'created_on']

    def __str__(self):
        return self.name

    @cached_property
    def campaign_urls(self):
        return list(self.actions.values_list('url', flat=True))
