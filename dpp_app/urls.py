from django.urls import path
from .views import check_event

urlpatterns = [
    path('api/events/', check_event, name='check_event'),
]