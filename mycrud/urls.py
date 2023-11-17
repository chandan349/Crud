from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('add_item', add_item, name='add_item'),
]