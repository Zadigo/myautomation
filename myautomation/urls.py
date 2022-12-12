from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('campaigns/', include('campaigns.urls')),
    path('admin/', admin.site.urls),
]
