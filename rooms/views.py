from datetime import datetime
from django.shortcuts import render
from . import models

# from django.http import HttpResponse


def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms})


# test view
def test(request):
    # return HttpResponse(content="<h1>hello</h1>")
    now = datetime.now()
    hungry = False
    return render(request, "test.html", context={"now": now, "hungry": hungry})
