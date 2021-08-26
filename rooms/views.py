from django.shortcuts import render

# from django.http import HttpResponse


def all_rooms(request):
    # return HttpResponse(content="<h1>hello</h1>")
    return render(request, "all_rooms")
