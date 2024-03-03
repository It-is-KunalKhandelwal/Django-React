from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    
    return HttpResponse("Hello, world. ")
def polls(request):
    print(request)
    print(HttpResponse("welcome to polls."))
    return HttpResponse("welcome to polls.")