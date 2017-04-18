from django.db import models
from common import IDGeneratedModel


class TopicListModel(IDGeneratedModel):
    title = models.CharField(max_length=256)
    author_id = models.IntegerField()
    content = models.TextField()
    deleted = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(blank=True, null=True)
    node_id = models.ForeignKey(
        'TopicNodeModel', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'topic_list'
        ordering = ('-updated_time',)


class TopicDetailModel(IDGeneratedModel):
    topic_id = models.ForeignKey('TopicListModel', on_delete=models.CASCADE)
    author_id = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = 'topic_detail'
        ordering = ('created_time',)
