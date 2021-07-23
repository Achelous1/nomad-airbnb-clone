# Airbnb core application
* 공통적인 부분을 담는 application
* 공통적으로 extend되어 사용하는 model class에는 하위처럼 작성한다

```python
class CustomModel(models.Model):

    """ Custom Model """

    class Meta:
        abstract = True # 추상모델로 변경하는 방법

```

* 상위처럼 작성하면 데이터베이스에 모델데이터가 생성되지 않는다