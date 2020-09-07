from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def math(request):
    return HttpResponse('Tu będzie matma')


def add(request, a, b):
    a, b = int(a), int(b)
    wynik = a + b
    c = {'a': a, 'b': b, 'operacja': '+', 'wynik': wynik, 'title': 'dodawanie'}
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


def sub(request, a, b):
    a, b = int(a), int(b)
    wynik = a - b
    c = {'a': a, 'b': b, 'operacja': '-', 'wynik': wynik, 'title': 'odejmowanie'}
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


def mul(request, a, b):
    a, b = int(a), int(b)
    wynik = a * b
    c = {'a': a, 'b': b, 'operacja': '*', 'wynik': wynik, 'title': 'mnożenie'}
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


def div(request, a, b):
    a, b = int(a), int(b)
    if b == 0:
        return HttpResponse('Nie dziel przez zero!')
    wynik = a / b
    c = {'a': a, 'b': b, 'operacja': '/', 'wynik': wynik, 'title': 'dzielenie'}
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )
