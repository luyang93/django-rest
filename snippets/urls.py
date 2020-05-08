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

    path('snippets_apiview/', views.snippet_list_apiview, name='snippet_list_apiview'),
    path('snippets_apiview/<int:pk>/', views.snippet_detail_apiview, name='snippet_detail_apiview'),
    path('snippets_apiview/<int:pk>/highlight/', views.snippet_highlight_apiview, name='snippet_highlight_apiview'),
    path('users_apiview/', views.user_list_apiview, name='user_list_apiview'),
    path('users_apiview/<int:pk>/', views.user_detail_apiview, name='user_detail_apiview'),

])
