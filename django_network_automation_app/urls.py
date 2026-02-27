"""
URL configuration for django_network_automation_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from devices.views import DeviceViewSet
from jobs.views import PlaybookJobViewSet
from cml_integration.views import CMLSettingsViewSet

router = DefaultRouter()
router.register(r"devices", DeviceViewSet, basename="devices")
router.register(r"jobs", PlaybookJobViewSet, basename="jobs")
router.register(r"cml-settings", CMLSettingsViewSet, basename="cml-settings")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
