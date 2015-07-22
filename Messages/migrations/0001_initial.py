# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, serialize=False, primary_key=True)),
                ('source', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date_rec', models.DateTimeField(auto_now_add=True)),
                ('date_mod', models.DateTimeField(auto_now=True)),
                ('rec_by', models.CharField(max_length=200)),
                ('response', models.TextField()),
            ],
        ),
    ]
