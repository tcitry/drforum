from django.contrib.auth.models import User
from django.db import models
from common.models import IDGeneratedModel, IDAutoAddModel


class TopicModel(IDAutoAddModel):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    deleted = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(blank=True, null=True)
    node_id = models.ForeignKey(
        'TopicNodeModel', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-updated_time',)

    def __str__(self):
        return self.title


class TopicCommentModel(IDAutoAddModel):
    topic = models.ForeignKey('TopicModel', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()

    class Meta:
        ordering = ('created_time',)

    def __str__(self):
        return self.topic.title


class TopicNodeModel(IDGeneratedModel):
    node_name = models.CharField(max_length=20)
    create_user_id = models.IntegerField()

    class Meta:
        ordering = ('created_time',)
