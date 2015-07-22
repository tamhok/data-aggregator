from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^test', views.test),
    url(r'^answer/', views.answer),
    url('^', include('django.contrib.auth.urls')),
]
