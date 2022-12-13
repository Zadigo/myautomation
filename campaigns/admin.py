from django.contrib import admin
from campaigns.models import Campaign, Action


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'runned', 'paused']
    date_hierarchy = 'created_on'
    filter_horizontal = ['actions']
    search_fields = ['name']


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['url', 'runned']
    date_hierarchy = 'created_on'
