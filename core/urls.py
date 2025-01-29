from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view=frontPage, name='frontpage'),
    path('shop/', view=shop, name='shop'), 
]