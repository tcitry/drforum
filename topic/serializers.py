from rest_framework import serializers
from . import models


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopicModel
        fields = '__all__'
        read_only_fields = ('id', 'author_id')


class TopicCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopicCommentModel
        fields = '__all__'
        read_only_fields = ('id', 'topic', 'author_id')
