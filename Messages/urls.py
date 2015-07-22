from django.conf.urls import urls

from . import views

urlpatterns = [
    url(r'^facebook/', views.facebook),
    url(r'^twitter/', views.twitter),
    url(r'^whatsapp/', views.whatsapp),
    url(r'^answer', views.answer),
]
