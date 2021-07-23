from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # 데이터생성 시 현재시간으로 insert
    updated = models.DateTimeField(auto_now=True)  # 데이터수정 시 현재시간으로 update

    class Meta:
        # abstract가 True 일 경우 해당 모델은 Database에 create하지 않는다
        abstract = True
