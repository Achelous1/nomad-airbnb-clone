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

## Pipenv
* Python에서 기본적으로 제공하는 PIP(Python Package Installer)에서 설치한 패키지는 글로벌*global*하게 설치되어 각 프로젝트별로 패키지를 관리할 수 없다
* 위의 단점을 보완하기 위해 나온것이 Pipenv이며 각 프로젝트 별로 버블*bubble*을 생성하여 패키지를 프로젝트 단위로 관리할 수 있게 해준다

### 설치 방법
```
# MacOS
$ brew install pipenv
$ brew upgrade pipenv

# Terminal
$ pip install --user pipenv
```

### Pipenv 버블 설정 방법
* Django는 Python3.x 버전에서 가장 잘 작동한다. 그러니 pipenv를 설정할 때 python3.x버전을 사용하게 option을 줘야한다

```
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

### Django 프로젝트 생성
1. `pipenv shell`
2. 먼저 `django-admin startproject config`로 `config` 프로젝트 생성
3. 다음 `config/config`폴더와 `config/manage.py`파일을 프로젝트의 최상위로 이동
4. `python manage.py migrate`
5. `python manage.py runserver`로 장고서버 실행
6. `python manage.py superuser`로 관리자 생성
