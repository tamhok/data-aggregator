from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^analytics/', views.analytics),
    url(r'^answer/$', views.answer),
    url(r'^answer/(?P<uuid>[a-f,0-9,-]+)/cancel$', views.answercancel),
    url(r'^answer/(?P<uuid>[a-f,0-9,-]+)/$', views.answerentry),
    url('^', include('django.contrib.auth.urls')),
]
