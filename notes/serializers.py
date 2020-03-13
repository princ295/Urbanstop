from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Note


class noteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['url', 'pk', 'ref', 'textnote', 'create', 'update']

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'