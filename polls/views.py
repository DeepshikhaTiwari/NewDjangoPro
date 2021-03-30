from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello ths is my first view, and you are at the poll index.")


def detail(request, question_id):
    return HttpResponse("You are looking at question %s." %question_id)


def results(request, question_id):
    response = "You are looking at result of quesion %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." %question_id)
