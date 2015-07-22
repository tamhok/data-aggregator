from django.contrib import admin

from .models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    fields = ['source', 'name', 'message']

admin.site.register(Message)

