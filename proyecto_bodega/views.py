from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name="inicio.html",
        context=contexto,
    )
    return http_response

def acerca_de_mi(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name="acerca.html",
        context=contexto,
    )
    return http_response