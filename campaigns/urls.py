from django.urls import re_path
from campaigns import views

app_name = 'campaigns'

urlpatterns = [
    re_path(
        r'^update/(?P<campaign_id>[a-zA-Z0-9]+)/state$', views.change_campaign_state_view),
    re_path(r'^run/(?P<campaign_id>[a-zA-Z0-9]+)$', views.run_campaign_view),
    re_path(
        r'^update/(?P<campaign_id>[a-zA-Z0-9]+)$', views.update_campaign_view),
    re_path(
        r'^delete/(?P<campaign_id>[a-zA-Z0-9]+)$', views.delete_campaign_view),
    re_path(r'^create$', views.create_campaign_view),
    re_path(r'^list$', views.list_campaign_view),

    re_path(r'^test', views.test_view)
]
