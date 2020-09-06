from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def helloWorld(request):
    return HttpResponse('Hello World!')


def helloWorldName(request, name):
    return HttpResponse('Hello' + ' ' + name.capitalize() + '!')
