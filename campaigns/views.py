from algorithm.requestors import Algorithm
from algorithm.utils import get_settings_for_parsed_website
from campaigns.models import Campaign
from campaigns.serializers import CampaignSerializer, CreateCampaignSerializer, CampaignStatus
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['get'])
def list_campaign_view(request, **kwargs):
    """Returns the user's list of campaigns
    >>> [{id: ..., name: ..., ....}]"""
    # query = request.GET
    campaigns = Campaign.objects.all()
    serialized_campaigns = CampaignSerializer(instance=campaigns, many=True)
    return Response(data=serialized_campaigns.data)


@api_view(['post'])
def create_campaign_view(request, **kwargs):
    """Creates a new campaign"""
    serializer = CreateCampaignSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return serializer.save(request)


@api_view(['post'])
def update_campaign_view(request, campaign_id, **kwargs):
    """Updates a created campaign"""
    instance = get_object_or_404(Campaign, id=campaign_id)
    campaign = CreateCampaignSerializer(instance=instance)
    campaign.is_valid(raise_exception=True)
    return campaign.update()


@api_view(['post'])
def run_campaign_view(request, campaign_id, **kwargs):
    """Runs a created campaign"""
    result = {}
    campaign = get_object_or_404(Campaign, id=campaign_id)
    instance = Algorithm(campaign)

    if campaign.parse_all_tables:
        pass
    elif campaign.parse_all_text:
        result = instance.parse_all_text()
    else:
        # Try to identify the website the user
        # is trying to parse from the list, and
        # then use the manual identification
        # to try and get the most interesting
        # section of the website
        website_settings = get_settings_for_parsed_website('example.com')
        if website_settings is None:
            # Just parse everything on the page
            pass
        else:
            if not website_settings.has_sections:
                # Just parse everything on the page
                pass
            else:
                # for section in website_settings:
                #     result = instance.parse_distinct(**section)
                result = instance.parse_distinct(website_settings['section'])

    if not campaign.runned:
        campaign.runned = True
        campaign.draft = False
        campaign.save()

    return Response(data={'result': result})


@api_view(['post'])
def delete_campaign_view(request, campaign_id, **kwargs):
    campaign = get_object_or_404(Campaign, id=None)
    return Response(data={})


@api_view(['post'])
def change_campaign_state_view(request, campaign_id, **kwargs):
    serializer = CampaignStatus(data=request.data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


@api_view(['post'])
def test_view(request, **kwargs):
    campaign = get_object_or_404(Campaign, id=11)
    algorithm = Algorithm(campaign)
    result = algorithm.parse_tables()
    return Response(result)
