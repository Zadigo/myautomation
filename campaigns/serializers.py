from campaigns.models import Campaign
from django.shortcuts import get_object_or_404
from rest_framework import fields
from rest_framework.exceptions import ValidationError
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
    urls = fields.CharField()
    campaign_urls = fields.ListField()
    results_per_search = fields.IntegerField()
    csv_file = fields.FileField()
    retries = fields.IntegerField()
    section_to_parse = fields.CharField()
    parse_all_tables = fields.BooleanField()
    parse_all_text = fields.BooleanField()
    runned = fields.BooleanField(default=False)
    paused = fields.BooleanField(default=False)
    archived = fields.BooleanField(default=False)
    draft = fields.BooleanField(default=True)
    created_on = fields.DateTimeField()


class CreateCampaignSerializer(Serializer):
    name = fields.CharField()
    urls = fields.CharField(allow_null=True)
    results_per_search = fields.IntegerField(default=100)
    csv_file = fields.FileField(allow_null=True)
    retries = fields.IntegerField(default=0)
    section_to_parse = fields.CharField(allow_null=True)
    parse_all_tables = fields.BooleanField(default=False)
    parse_all_text = fields.BooleanField(default=False)
    draft = fields.BooleanField(default=True)

    def save(self, request, **kwargs):
        urls = self.validated_data['urls']
        file = self.validated_data['csv_file']

        if urls is None and file is None:
            raise ValidationError(detail={
                'urls': {
                    'message': 'No urls were provided'
                },
                'csv_fil': {
                    'message': 'No file was provided'
                }
            })

        Campaign.objects.create(**self.validated_data)
        queryset = Campaign.objects.all()
        serializer = CampaignSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)

    def update(self, instance):
        instance.update(**self.validated_data)
        return Response(data={})
