from rest_framework import serializers
from .. import models


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopicModel
        fields = ('id', 'title', 'author_id', 'content')
