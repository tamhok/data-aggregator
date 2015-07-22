from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from . import models
from . import twitter_converter
from django.http import HttpResponse, HttpRequest
import logging
# Create your views here.

logger = logging.getLogger(__name__)

@require_http_methods(["POST"])
def facebook(request):
    return HttpResponse("201")

@require_http_methods(["POST"])
def twitter(request):
    return HttpResponse("201")


def test(request):
    return HttpResponse("Testing ")

@require_http_methods(["POST"])
def whatsapp(request):
    return HttpResponse("200")

@login_required()
def answer(request):
    return HttpResponse("200")
