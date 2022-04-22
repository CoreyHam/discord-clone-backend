from .models import Category, Server, Channel, Relationship, Message
from django.contrib.auth.models import User
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at')

class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'name', 'created_at', 'created_by', 'users')

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name', 'description', 'server', 'category', 'created_at', 'updated_at')

class RelationshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relationship
        fields = ('id', 'user', 'is_friend')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'content', 'channel', 'sent_by', 'created_at', 'updated_at')