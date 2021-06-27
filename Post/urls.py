# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('view/<int:pk>', views.PostDetail.as_view(), name='post_view'),
    path('new', views.PostCreate.as_view(), name='post_new'),
]