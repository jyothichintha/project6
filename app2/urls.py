from app2.views import *
from django.urls import path
app_name='ntg'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('rahul/',rahul,name='rahul'),
]