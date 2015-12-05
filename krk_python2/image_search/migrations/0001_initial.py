# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.ImageField(upload_to=b'images/%Y/%m/%d')),
                ('request_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
