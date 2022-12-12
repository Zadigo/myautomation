from campaigns.models import Campaign
from django.shortcuts import get_object_or_404
from rest_framework import fields
from rest_framework.response import Response
from rest_framework.serializers import Serializer


class CampaignStatus(Serializer):
    id = fields.IntegerField()
    runned = fields.BooleanField(default=False)
    paused = fields.BooleanField(default=False)
    archived = fields.BooleanField(default=False)
    draft = fields.BooleanField(default=True)

    def save(self, **kwargs):
        campaign = get_object_or_404(Campaign, id=self.validated_data['id'])
        data = self.validated_data.copy()
        data.pop('id')
        campaign.update(**data)
        serializer = CampaignStatus(instance=campaign)
        return Response(data=serializer.data)


class CampaignSerializer(Serializer):
    id = fields.IntegerField()
    name = fields.CharField()
    runned = fields.BooleanField(default=False)
    paused = fields.BooleanField(default=False)
    archived = fields.BooleanField(default=False)
    draft = fields.BooleanField(default=True)
    created_on = fields.DateTimeField()


class CreateCampaignSerializer(Serializer):
    name = fields.CharField()

    def save(self, request, **kwargs):
        instance = Campaign.objects.create(**self.validated_data)
        queryset = Campaign.objects.all()
        serializer = CreateCampaignSerializer(data=queryset)
        return Response(data=serializer.data)

    def update(self, instance):
        instance.update(**self.validated_data)
        return Response(data={})
