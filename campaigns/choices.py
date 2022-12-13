from django.db.models import Choices


class WebRequests(Choices):
    GET = 'GET'
    POST = 'POST'
