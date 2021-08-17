from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns=[
    path('app1_fir/',app1_fir,name='app1_fir'),
]