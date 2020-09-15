from django.urls import path
from testapp import views
import os

#template tagging
app_name = 'testapp'

urlpatterns = [

path('relative/', views.relative,name='relative'),
path('other/', views.other,name='other'),
]
