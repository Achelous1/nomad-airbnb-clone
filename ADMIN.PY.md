# admin.py 에 대하여
* admin.py는 해당 모델 객체를 어드민 패널에서 어떻게 사용할 것인가 설정하는 파이썬 파일이다
* 해당 어드민 클래스의 옵션들은 [Django Admin Options](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)에서 참고하자

|화면| 옵션   | 설명   | 비고   |
|----|----|----|----|
|리스트| list_display | 어드민 패널의 리스트에 보여질 컬럼/필드   |    |
|리스트| list_filter| 어드민 패널의 오른쪽에 나타나며, 해당 필드의 필터링을 담당한다 | |
|리스트| search_fields| 리스트에서 검색 시 어떤 필드들에 관해서 검색을 할 것인지 설정한다|[참조](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)|
|에디트| fieldsets | 어드민패널의 수정화면에서 필드셋 그룹핑을 담당한다 |  |
|에디트| filter_horizontal| MtoM관계의 필드들을 양쪽으로 add/remove할 수 있는 인터페이스로 변경해준다||
|에디트 |raw_id_fields|할당된 필드를 팝업리스트 형태로 열어 검색하여 선택할 수 있게 해주는 옵션이다| |

## Inline Models
* 특정 모델에 대한 manipulation을 다른 모델어드민으로 끌어와서 사용할 수 있게 해주는 기능이다
* 예제 코드 ([실제 적용 부분](./rooms/admin.py)) :
```py
# 다른 어드민에 넣을 모델의 클래스
# StackedInline 등 다른 형식으로 보여줄 수도 있음
class PhotoInline(admin.TabularInline):

    model = models.Photo

# 적용할 어드민 패널
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    inlines = (PhotoInline,)
```
