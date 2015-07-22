from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'converter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^messages/', include('messages.url')
    url(r'^admin/', include(admin.site.urls)),
)
