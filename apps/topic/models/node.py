from django.db import models
from common import IDGeneratedModel


class TopicNodeModel(IDGeneratedModel):
    node_name = models.CharField(max_length=20)
    create_user_id = models.IntegerField()

    class Meta:
        db_table = 'topic_node'
        ordering = ('created_time',)
