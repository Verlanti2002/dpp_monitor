from django.urls import path
from .views import receive_event

urlpatterns = [
    path('api/events/', receive_event, name='receive_event'),
]