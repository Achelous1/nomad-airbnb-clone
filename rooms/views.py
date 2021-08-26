from datetime import datetime
from django.shortcuts import render

# from django.http import HttpResponse


def all_rooms(request):
    # return HttpResponse(content="<h1>hello</h1>")
    now = datetime.now()
    hungry = False
    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
