"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# settings.py를 임포트할 때엔 루트에서 바로 임포트하는것이 아닌 django.conf 패키지 내에서 임포트한다
from django.conf import settings

# MEDIA_URL과 MEDIA_ROOT를 연결해주는 패키지를 임포트
from django.conf.urls.static import static

urlpatterns = [path("admin/", admin.site.urls)]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
