from django.urls import path
from .views import *


urlpatterns = [
    path('', view=home, name='twitter-home')
]