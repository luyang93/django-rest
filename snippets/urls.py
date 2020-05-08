# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views
from snippets.views import SnippetViewSet, UserViewSet, api_root

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns += format_suffix_patterns([
    path('', api_root),

    path('snippets_csrf/', views.snippet_list_csrf, name='snippet_list_csrf'),
    path('snippets_csrf/<int:pk>/', views.snippet_detail_csrf, name='snippet_detail_csrf'),
    path('snippets_csrf/<int:pk>/highlight/', views.snippet_highlight_csrf, name='snippet_highlight_csrf'),
    path('users_csrf/', views.user_list_csrf, name='user_list_csrf'),
    path('users_csrf/<int:pk>/', views.user_detail_csrf, name='user_detail_csrf'),
])
