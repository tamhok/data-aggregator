from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Message
from . import twitter_converter
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
import logging
import uuid
from .import broadcast_message
# Create your views here.

logger = logging.getLogger(__name__)

#Screen displaying the questions
@login_required()
def answer(request):
    topten = Message.objects.filter(rec_by__exact = "").order_by('date_rec')[:10]
    data = [dict([(str(tr.id), tr.message)]) for tr in topten]
    return HttpResponse(data)

#Screen displaying the text box for the answers
@login_required()
def answerentry(request, uuid):
    mobj = Message.objects.get(id__exact=uuid)
    if request.method == 'GET':
        if(mobj.rec_by == ""):
            mobj.rec_by = str(request.user)
            mobj.save()
            return HttpResponse("the file")
        else
            return HttpResponseRedirect('/Messages/answer')
    elif request.method == 'POST':
        mobj.response = request.POST['message']
        mobj.save()
        logger.info(broadcaster(mobj.source, mobj.name, mobj.message))
    return  HttpResponseRedirect('/Messages/answer')

@login_required()
def answercancel(request, uuid):
    mobj = Message.objects.get(id__exact=uuid)
    mobj.rec_by = ""
    mobj.save()
    return  HttpResponseRedirect('/Messages/answer')

def analytics(request):
    return HttpResponse('Great')
