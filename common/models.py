from django.db import models


class BaseDateTimeModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class IDGeneratedModel(BaseDateTimeModel):
    id = models.CharField(max_length=128, primary_key=True)

    class Meta:
        abstract = True
