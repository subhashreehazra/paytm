# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0002_auto_20170309_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNID',
            field=models.CharField(max_length=30, verbose_name=b'TXN ID'),
        ),
    ]
