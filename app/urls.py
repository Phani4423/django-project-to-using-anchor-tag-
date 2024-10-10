from django.urls import path
from app.views import *
urlpatterns = [
    path('fun/',fun,name='fun'),
]