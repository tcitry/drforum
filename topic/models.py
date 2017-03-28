from django.db import models
from common import IDGeneratedModel, BaseDateTimeModel


class TopicListModel(IDGeneratedModel):
    title = models.CharField(max_length=256)
    content = models.TextField()
    deleted = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(blank=True, null=True)
    node_id = models.ForeignKey('TopicNodeModel', on_delete=models.SET_NULL, null=True)

    class Mate:
        db_table = 'topic_list'
        ordering = ('-updated_time',)


class TopicDetailModel(BaseDateTimeModel):
    topic_id = models.ForeignKey('TopicListModel', on_delete=models.CASCADE)
    comment = models.TextField()

    class Mate:
        db_table = 'topic_detail'
        ordering = ('created_time',)


class TopicNodeModel(BaseDateTimeModel):
    node_name = models.CharField(max_length=20)

    class Mate:
        db_table = 'topic_node'
        ordering = ('created_time')
