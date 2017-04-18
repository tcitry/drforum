from django.db import models
from common import IDAutoAddModel


class TopicModel(IDAutoAddModel):
    title = models.CharField(max_length=256)
    author_id = models.IntegerField()
    content = models.TextField()
    deleted = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(blank=True, null=True)
    node_id = models.ForeignKey(
        'TopicNodeModel', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'topics'
        ordering = ('-updated_time',)


class TopicCommentModel(IDAutoAddModel):
    topic_id = models.ForeignKey('TopicModel', on_delete=models.CASCADE)
    author_id = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = 'topic_comments'
        ordering = ('created_time',)
