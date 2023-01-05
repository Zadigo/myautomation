from django.db.models import Choices


class WebRequests(Choices):
    GET = 'GET'
    POST = 'POST'


class Operators(Choices):
    pass
