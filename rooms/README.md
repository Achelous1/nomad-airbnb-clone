# Airbnb rooms application
* Django의 Rooms 부분을 담는 application
* countries 항목은 `Django countries` 라이브러리를 사용한다
    * `pipenv install django-countries` 로 설치
    * `settings.py`파일의 `THIRD_PARTY_APPS`에 `django_countries`항목 추가
* Room 클래스와 User 클래스를 foreign key로 연결 (1:m 관계)
* Room 클래스와 각 Room type 등을 Abstract Item을 통해 many to many(m:m)으로 연결
* Room type 등을 admin.py에 @admin.register 데코레이터로 추가하여 어드민패널에서 CRUD가 가능하다