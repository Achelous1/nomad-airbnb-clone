# Django Airbnb 클론코딩
* 2021년 7월에 시작한 NomadCoders의 Django Airbnb 클론코딩
* 해당 프로젝트는 Django 2.2.5 버전을 사용

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

### Django 프로젝트 생성
1. 먼저 `django-admin startproject config`로 `config` 프로젝트 생성
2. 다음 `config/config`폴더와 `config/manage.py`파일을 프로젝트의 최상위로 이동
3. 