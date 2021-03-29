from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello ths is my first view, and you are at the poll index.")
