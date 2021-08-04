# models.py에 대하여
* `models.py`에서는 특정 클래스에 대하여 데이터베이스에 등록하는 것 뿐만 아니라 데이터베이스에서 가져올 때,QuerySet이란 클래스로 담겨와서 해당 클래스로써 사용할 수도 있다.
* `model`클래스에 사전정의 돼있는 메서드를 override 하기 위하여 [참조](https://docs.djangoproject.com/en/3.2/topics/db/models/#overriding-predefined-model-methods)