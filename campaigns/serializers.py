from campaigns.choices import WebRequests
from campaigns.models import Campaign, Action
from django.shortcuts import get_object_or_404
from rest_framework import fields
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from campaigns.utils import split_values


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


class ActionSerializer(Serializer):
    id = fields.IntegerField()
    url = fields.URLField()
    web_request = fields.ChoiceField(WebRequests.choices)
    runned = fields.BooleanField()


class CampaignSerializer(Serializer):
    id = fields.IntegerField()
    actions = ActionSerializer(many=True)
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
    # data_constraint = fields.ListField()
    results_per_search = fields.IntegerField(default=100)
    csv_file = fields.FileField(allow_null=True)
    retries = fields.IntegerField(default=0)
    section_to_parse = fields.CharField(allow_null=True)
    parse_all_tables = fields.BooleanField(default=False)
    parse_all_text = fields.BooleanField(default=True)
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

        campaign = Campaign.objects.create(**self.validated_data)
        splitted_urls = split_values(urls)
        for url in splitted_urls:
            campaign.actions.create(url=url)
        
        queryset = Campaign.objects.all()
        serializer = CampaignSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)

    def update(self, instance):
        instance.update(**self.validated_data)
        return Response(data={})
