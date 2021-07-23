from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        # abstract가 True 일 경우 해당 모델은 Database에 create하지 않는다
        abstract = True
