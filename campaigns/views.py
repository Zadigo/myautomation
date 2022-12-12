from algorithm.requestors import Algorithm
from campaigns.models import Campaign
from campaigns.serializers import CreateCampaignSerializer, CampaignSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['get'])
def list_campaign_view(request, **kwargs):
    query = request.GET
    campaigns = Campaign.objects.all()
    serialized_campaigns = CampaignSerializer(instance=campaigns, many=True)
    return Response(data=serialized_campaigns.data)


@api_view(['post'])
def create_campaign_view(request, **kwargs):
    campaign = CreateCampaignSerializer(data=request.data)
    campaign.is_valid(raise_exception=True)
    return campaign.save(request)


@api_view(['post'])
def update_campaign_view(request, campaign_id, **kwargs):
    instance = get_object_or_404(Campaign, id=campaign_id)
    campaign = CreateCampaignSerializer(instance=instance)
    campaign.is_valid(raise_exception=True)
    return campaign.update()


@api_view(['post'])
def run_campaign_view(request, campaign_id, **kwargs):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    instance = Algorithm(campaign)
    result = instance.parse_distinct('h1')
    return Response(data={'result': result})


@api_view(['post'])
def delete_campaign_view(request, campaign_id, **kwargs):
    campaign = get_object_or_404(Campaign, id=None)
    return Response(data={})


@api_view(['post'])
def change_campaign_state_view(request, campaign_id, **kwargs):
    campaign = get_object_or_404(Campaign, id=None)
    return Response(data={})
