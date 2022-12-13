import csv
import time

import requests
from algorithm import html_models
from algorithm.mixins import CleaningMixin
from algorithm.utils import get_default_proxies, get_random_header
from bs4 import BeautifulSoup
from nltk.tokenize import TweetTokenizer

# from django.core.files import File


class HTTPRequest:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.resolved = False
        self.errors = []

    def __repr__(self):
        return f'{self.__class__.__name__}(url={self.url}, resolved={self.resolved})'

    def _send(self):
        session, prepared_request = self.create_session(
            method='get',
            url=self.url,
            headers=self.prepare_headers()
        )
        try:
            response = session.send(prepared_request)
        except Exception as e:
            self.errors.append(e.args)
        else:
            if response.status_code == 200:
                self.resolved = True
                self.response = response.content
            else:
                self.errors.append((f'Request failed with code {response.status_code}'))

    def prepare_headers(self, **headers):
        return {
            **headers,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Accept-Language': 'fr,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,en-GB;q=0.6',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }

    def before_send(self, **params):
        return params

    def create_session(self, **params):
        session = requests.Session()
        # session.proxies
        request = requests.models.Request(
            **self.before_send(**params)
        )
        return session, session.prepare_request(request)


class RequestQueue:
    def __init__(self):
        self.urls = []

    def __get__(self, instance, cls=None):
        # Get the urls that we are going to use
        # in order to parse their pages
        self.urls = instance.campaign.campaign_urls
        return [HTTPRequest(url) for url in self.urls]


class Algorithm(CleaningMixin):
    request_queue = RequestQueue()

    def __init__(self, campaign, proxies=[]):
        self.campaign = campaign
        self.proxies = get_default_proxies()
        self._headers = {}

    def resolve_all(self):
        items = []
        for request in self.request_queue:
            if not request.resolved:
                request._send()
                time.sleep(5)
                items.append(BeautifulSoup(request.response, 'html.parser'))
        return items

    def parse_all_text(self):
        """Returns all the text from a given page"""
        soups = self.resolve_all()
        for soup in soups:
            yield soup.get_text()

    def parse_tables(self):
        """Returns all the data present in all
        the tables from a given page"""
        for soup in self.resolve_all():
            tables = soup.find_all('table')
            if len(tables) == 0:
                break
            for table in tables:
                yield html_models.TableObject(table)

    def parse_distinct(self, tag=None, **attrs):
        """Parse a distinct element on the
        given HTML page"""
        instance = TweetTokenizer()
        soups = self.resolve_all()
        for soup in soups:
            item = soup.find(tag, **attrs)
            if item is None:
                continue
            yield self.clean(item.getText())
