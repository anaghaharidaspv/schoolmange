from django.urls import path
from .views import *
app_name='chat'


urlpatterns = [
    path('lobby/',lobby.as_view(),name='lobby')
]
