from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from . import models
# Create your views here.

@require_http_methods(["POST"])
def facebook(request):

    return HttpResponse("201")

@require_http_methods(["POST"])
def twitter(request):

    return HttpResponse("201")

@require_http_methods(["POST"])
def whatsapp(request):

    return HttpResponse("200")

@require_http_methods(["GET"])
def answer(request):

    return HttpResponse("200")
