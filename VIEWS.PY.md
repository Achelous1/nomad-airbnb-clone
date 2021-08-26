# views.py에 대하여
* view는 function이다
* http로 request 가 들어오면 response를 다시 반환하는 일련의 과정이 담긴 함수다
* render함수를 반환할 시에는 [settings.py](./config/settings.py)에 정의된 템플릿 폴더에 있는 해당 [html파일](./templates/all_rooms.html)을 찾아 django가 렌더링 한 후에 해당 html을 리턴한다
* template을 사용 할 경우 django의 view에서 넘겨준 context는 `{{expression}}`으로 사용할 수 있다.
* 로직 등의 표현을 사용하고자 할 때에는 `{% 로직명 %}`으로 사용할 수 있다.