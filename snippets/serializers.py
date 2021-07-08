# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import serializers

from snippets.models import Snippet

User = get_user_model()


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet_highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']
        extra_kwargs = {'url': {'view_name': 'snippet_detail'}}


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet_detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'name', 'snippets']
        extra_kwargs = {'url': {'view_name': 'user_detail'}}
