from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")



def v2(request):
    return HttpResponse("View2")


def login(request):
    return HttpResponse("login Screen")