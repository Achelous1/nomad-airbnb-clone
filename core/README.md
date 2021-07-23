# Airbnb core application
* 공통적인 부분을 담는 application
* 공통적으로 extend되어 사용하는 model class에는 하위처럼 작성한다

```py
class CustomModel(models.Model):

    """ Custom Model """

    class Meta:
        abstract = True # 추상모델로 변경하는 방법

```

* 상위처럼 작성하면 데이터베이스에 모델데이터가 생성되지 않는다

* 상속할 때엔 해당 코어라이브러리의 클래스를 import애서 사용한다

```py
from django.db import models
from core import models as core_models


class Room(core_models.TimeStampedModel):

    """Rooms Model Definition"""
```