from . import views
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('healthcheck', views.health_check),
]