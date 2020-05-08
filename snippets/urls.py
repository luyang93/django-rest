# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views
from snippets.views import SnippetViewSet, UserViewSet, api_root

snippet_list_viewset = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail_viewset = SnippetViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight',
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list_viewset = UserViewSet.as_view({
    'get': 'list'
})
user_detail_viewset = UserViewSet.as_view({
    'get': 'retrieve'
})

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

    path('snippets_class/', views.SnippetList.as_view(), name='SnippetList'),
    path('snippets_class/<int:pk>/', views.SnippetDetail.as_view(), name='SnippetDetail'),
    path('snippets_class/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='SnippetHighlight'),
    path('users_class/', views.UserList.as_view(), name='UserList'),
    path('users_class/<int:pk>/', views.UserDetail.as_view(), name='UserDetail'),

    path('snippets_mixin/', views.SnippetListMixin.as_view(), name='SnippetListMixin'),
    path('snippets_mixin/<int:pk>/', views.SnippetDetailMixin.as_view(), name='SnippetDetailMixin'),
    path('snippets_mixin/<int:pk>/highlight/', views.SnippetHighlightMixin.as_view(), name='SnippetHighlightMixin'),
    path('users_mixin/', views.UserListMixin.as_view(), name='UserListMixin'),
    path('users_mixin/<int:pk>/', views.UserDetailMixin.as_view(), name='UserLDetailMixin'),

    path('snippets_generics/', views.SnippetListGenerics.as_view(), name='SnippetListGenerics'),
    path('snippets_generics/<int:pk>/', views.SnippetDetailGenerics.as_view(), name='SnippetDetailGenerics'),
    path('snippets_generics/<int:pk>/highlight/', views.SnippetHighlightGenerics.as_view(), name='SnippetHighlightGenerics'),
    path('users_generics/', views.UserListGenerics.as_view(), name='UserListGenerics'),
    path('users_generics/<int:pk>/', views.UserDetailGenerics.as_view(), name='UserDetailGenerics'),

    path('snippets_viewset/', snippet_list_viewset, name='snippet_list'),
    path('snippets_viewset/<int:pk>/', snippet_detail_viewset, name='snippet_detail'),
    path('snippets_viewset/<int:pk>/highlight/', snippet_highlight, name='snippet_highlight'),
    path('users_viewset/', user_list_viewset, name='user_list'),
    path('users_viewset/<int:pk>/', user_detail_viewset, name='user_detail'),
])
