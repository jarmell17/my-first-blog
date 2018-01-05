# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:58:56 2018

@author: jarmell
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]