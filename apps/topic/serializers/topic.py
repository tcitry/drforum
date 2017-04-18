from rest_framework import serializers
from .. import models


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopicListModel
        fields = ('id', 'title', 'author_id', 'content')
