from django.db import models
import uuid
# Create your models here.

class Message(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    source = models.CharField(max_length=200)
    name = models.CharField(max_length = 200)
    message = models.TextField()
    date_rec = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now = True)
    rec_by = models.CharField(max_length = 200)
    response = models.TextField()

    def __init__(self, source, name, message):
        self.source = source
        self.name = name
        self.message = message

    def __str__(self):
        return self.source + " " + self.name + " " + self.date_rec


