# Airbnb config application
* Django의 설정파일들을 담는 application
* settings.py의 INSTALLED_APPS에 application을 추가해야 해당 어플리케이션이 장고에서 로딩이 된다

``` python
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig",
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS
```