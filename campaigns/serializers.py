from rest_framework.serializers import Serializer
from rest_framework import fields
from campaigns.models import Campaign
from rest_framework.response import Response

class CampaignSerializer(Serializer):
    id = fields.IntegerField()
    name = fields.CharField()
    created_on = fields.DateTimeField()


class CreateCampaignSerializer(Serializer):
    name = fields.CharField()

    def save(self, request, **kwargs):
        instance = Campaign.objects.create(**self.validated_data)
        return Response(data={})

    def update(self, instance):
        instance.update(**self.validated_data)
        return Response(data={})
