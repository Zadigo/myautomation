from django.contrib import admin
from campaigns.models import Campaign

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'runned', 'paused']
    date_hierarchy = 'created_on'
