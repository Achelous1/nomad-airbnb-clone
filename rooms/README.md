# Airbnb rooms application
* Django의 Rooms 부분을 담는 application
* countries 항목은 `Django countries` 라이브러리를 사용한다
    * `pipenv install django-countries` 로 설치
    * `settings.py`파일의 `THIRD_PARTY_APPS`에 `django_countries`항목 추가
* Room 클래스와 User 클래스를 foreign key로 연결 (`1:m 관계`)
    * `on_delete` : 유저인스턴스가 삭제될 시 장고에서 데이터베이스로 명령할 행위이다 [참조](https://docs.djangoproject.com/ko/3.2/ref/models/fields/#foreignkey)
* Room 클래스와 각 Room type 등을 Abstract Item을 통해 many to many(`m:m 관계`)으로 연결
* Room type 등을 admin.py에 `@admin.register` 데코레이터로 추가하여 어드민패널에서 CRUD가 가능하다
* admin options [참조](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#modeladmin-options)
    * `list_display` : admin 리스트 테이블에서 보여줄 컬럼의 리스트
    * `list_filter` : admin 리스트 테이블 필터 항목
    * `search_fields` : admin 리스트에서 특정 항목들의 문자열을 검색할 수 있다.(case insensitive)[참조](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)
    * `__`로 object의 특정 필드를 검색할 수도 있음
    * `filter_horizontal` : 수정화면에서 add/remove로 항목을 움직일 수 있음
    * `fieldsets` : 수정화면에서 fieldset으로 각 필드들을 구분할 수 있음
* `model`의 `city`항목의 첫글자를 대문자로 바꾸려면 중간에 intercept를 통하여 구현