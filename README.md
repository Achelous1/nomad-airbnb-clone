# Django Airbnb 클론코딩
* 2021년 7월에 시작한 NomadCoders의 Django Airbnb 클론코딩
* 해당 프로젝트는 Django 2.2.5 버전을 사용

## Python
* Python은 런타임 언어이다.
    * 컴파일러가 존재하지 않는다. 그렇기 때문에 소스코드에 에러가 있어도 이것을 잡아내줄 방법이 없다는 뜻이다.
    * 위 단점을 보완하기 위해 사람들이 구현한 것이 `Linter`라는 프로그램
        * Linter는 파이썬 코드를 실행 전 해당 파이썬 프로젝트에 가이드라인 위반 등의 오류를 잡아준다
        * 해당 프로젝트에서는 `> Python : Select Linter -> flake8`을 사용할 것
        * 설치되어 있지 않다면 설치할 것
        * Linter에서 이미 deprecate된 항목들이 에러로 발생한다면, settings.json에서
            `"python.linting.flake8Args" : ["--max-line-length={lineLength}"]`
            을 추가해준다
    * Formatter
        * 자동으로 코드를 보기 좋게 형식에 맞춰주는 프로그램
        * 해당 프로젝트에서는 `black` 포맷터를 사용할 것
* PEP 8 *Python Enhancement Proposal* : Python의 코드 가이드라인/컨벤션
* vars & dir
    * `vars` : `__dict__`속성 즉 해당 모듈, 클래스, 인스턴스 또는 다른 모든 오브젝트의 딕셔너리 정보를 반환한다
    * `dir` : 인수없이 호출했을 때, 현재 로컬 스코프에 존재하는 name들의 리스트를 반환한다

## Pipenv
* Python에서 기본적으로 제공하는 PIP(Python Package Installer)에서 설치한 패키지는 글로벌*global*하게 설치되어 각 프로젝트별로 패키지를 관리할 수 없다
* 위의 단점을 보완하기 위해 나온것이 Pipenv이며 각 프로젝트 별로 버블*bubble*을 생성하여 패키지를 프로젝트 단위로 관리할 수 있게 해준다

### 설치 방법
```shell
# MacOS
$ brew install pipenv
$ brew upgrade pipenv

# Terminal
$ pip install --user pipenv
```

### Pipenv 버블 설정 방법
* Django는 Python3.x 버전에서 가장 잘 작동한다. 그러니 pipenv를 설정할 때 python3.x버전을 사용하게 option을 줘야한다

```shell
# Terminal
$ pipenv --three
```

* `pipenv shell` 명령어를 통해 pipenv의 버블 안으로 위치한다
* 이후 이 shell 내부에서 패키지를 설치하면 해당 프로젝트 내에서만 사용 가능한 패키지로 설치
    * 설치한 패키지의 의존성*dependency*는 `Pipfile`내부에 추가된다 (향후 해당 소스코드를 사용하는 다른 프로젝트에서도 사용가능)

## Django
* Django는 `pipenv install django=={version}`으로 설치한다
* 프로젝트를 생성할 때에는 `django-admin startproject {projectName}`명령어를 사용하여 설치한다
    * 위 방법은 매우 초심자-친화적이어서 이번 프로젝트 내에선 사용하지 않을것
* Django에서 기본적으로 생성해준 파일들의 주석들을 잘 보고 Document의 도움을 받을것
* Django프로젝트 
    * Django프로젝트는 기본적으로 application들의 묶음이다
    * Application은 function들의 묶음이다
    * 각 Application 별로 묶어서 관리
    * console에서 Django 환경으로 python 스크립트를 실행시키기 위해선 `python manage.py shell`로 접속하여 실행
    * 각 Application은 최대한 계획하여 서비스 별로 모듈화(작게)해서 만들 것
        * :thumbsup: Rule of Thumb : Application에 대해서 한문장으로 설명할 수 있어야 할 것!
* Django ORM(Object Relational Mapping)
    * Django는 ORM으로 데이터베이스와 통신한다

* Good Practices :
    1. import를 할 때에는 django/python 패키지 -> 써드파티 패키지 -> 커스텀 패키지 순으로 import 한다
    2. class에 필드를 정의할 때에는 기본적인 `데이터형식의 필드` -> `relational 필드(ForeignKey, ManyToMany 등)` -> `class Meta (메타 옵션)` -> `__str__` 등의 함수 순으로 작성하자
    3. `admin`에서만 사용되는 메서드가 아닌 전역으로 사용되는 메서드 같은 경우, `model`에 정의해서 사용한다
    4. `media`폴더/데이터베이스(sqlite)를 프로젝트 디렉터리 내부에서 작업하는 것은 개발단계에서만 할것. production 단계에서는 특정 스토리지/데이터베이스 레이어에서 모든 파일/데이터를 관리하게 하는 것이 옳다.

* Meta Class : 
    1. 상속 되지 않는 해당 클래스의 고유 메타정보를 담고 있는 클래스 [참조](https://docs.djangoproject.com/en/3.2/ref/models/options/)

* Console에서 Django 를 실행하여 스크립트를 짜볼 때 `python manage.py shell` 로써 실행한다.
* `manager` : Django의 모델 내부에 존재하여 데이터베이스와 통신할 수 있게 해주는 객체( == DAO? Mapper?)[참고](https://docs.djangoproject.com/en/3.2/topics/db/queries/)
* `QuerySet` : model object의 list이며 데이터를 쿼리함에 있어 유용한 객체 [참고](https://docs.djangoproject.com/en/3.2/ref/models/querysets/)
    * `filter()` : select where
    * `get()` : select one
    * `all()` : 모든 리스트 select
* Django ORM
    * ForeignKey : 해당 타겟의 `target.{model_name}_set`에서 조회가 가능하다

### Django 프로젝트 생성
1. `pipenv shell`
2. 먼저 `django-admin startproject config`로 `config` 설정폴더 생성
3. 다음 `config/config`폴더와 `config/manage.py`파일을 프로젝트의 최상위로 이동
4. `python manage.py makemigration`으로 migration 할 model 데이터 생성 
5. `python manage.py migrate`로 DB에 데이터 마이그레이션
6. `python manage.py runserver`로 장고서버 실행
7. `python manage.py superuser`로 관리자 생성

### Django Application 생성
1. `django-admin startapp {application명}` 명령어로 생성
    * rooms, users, reviews, conversations, lists, reservations 생성
    * 생성된 Application내부의 파일들의 이름은 ***절대로!!!*** 변경해서는 안된다 
        * Django에서 지정한 규칙대로 사용해야 하기 때문(Framework와 Library의 차이)
    * [`admin.py`](./ADMIN.PY.md) -> admin 패널에서 반영 될 코드
    * `apps.py` -> Application의 설정파일
    * [`models.py`](./MODELS.PY.md) -> 데이터베이스에 반영될 모델데이터
    * `tests.py` -> 테스트 파일
    * [`views.py`](./VIEWS.PY.md) -> 사용자가 보낸 request를 처리하여 다시 사용자에게 response를 해주는 파일
    * [`urls.py`](./URLS.PY.md) -> url을 처리해주는 파일

2. User model을 변경하는 방법 [참조](https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#substituting-a-custom-user-model)

3. Django에서 application을 settings.py의 `INSTALLED_APPS`에 추가하면 장고실행 시 읽어올 수 있다.
    * 기본적인 Django app들과 Project app을 분리해서 관리하면 편하다

4. models.py에선 기본적으로 해당 application에서 사용될 모델을 정의하는데 의의가 있다.
    * model의 유형에 관해서 [참조](https://docs.djangoproject.com/en/3.2/ref/models/fields/)
    * model에 클래스를 추가할 때마다 comment block `""" {model description} """` 을 추가해서 해당 모델이 어디에 사용되는지 입력할 수 있다
    * Python에서 `models.ImageField()`를 사용하려면 pillow란 플러그인을 사용해야 한다
    ``` pipenv install Pillow ```
    * charfield에서 값을 특정하고 싶다면 choices를 사용 (Users/models.py 참조)
    * 특정 모델에서 다른 모델과의 참조관계(foreign key)를 만들고 싶다면:
        1. 필드를 `models.ForeignKey()`로 정의
        2. 연결할 모델을 import하고 필드에 모델 및 옵션 넘겨주기 (rooms/models.py 참조)

### Django 커스텀 커맨드 생성
* `python manage.py {command} --{option}`의 형식으로 커스텀 커맨드를 생성하는 방법
* [Django document - Writing custom django-admin commands](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/)
* [작성 된 커스텀 커맨드 리스트](./rooms/management/commands)

### django_seed 패키지를 활용한 가짜 데이터 생성
* [django-seed 깃허브](https://github.com/Brobin/django-seed)
* [faker](https://faker.readthedocs.io/en/master/)