# Airbnb users application
* Django의 User를 담당하는 application
* Admin패널에서의 User를 상속하여 사용
    * models.py의 상속모델 참조
    * configs/settings.py에서 UserConfig 로딩 후 파일아래에 AUTH_USER_MODEL 부분 참조
