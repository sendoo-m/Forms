# Generated by Django 3.2 on 2022-11-04 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_candidate_situation'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=datetime.datetime(2022, 11, 4, 11, 28, 17, 911946, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='personality',
            field=models.CharField(choices=[('', 'select a personality'), ('I am outgoing', 'I am outgoing'), ('I am sociable', 'I am sociable'), ('I am antisocial', 'I am antisocial'), ('I am disceet', 'I am disceet'), ('I am serious', 'I am serious')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='salary',
            field=models.CharField(default=datetime.datetime(2022, 11, 4, 11, 29, 16, 236234, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='smoker',
            field=models.CharField(choices=[('1', 'Yes'), ('2', 'No')], default='No', max_length=10),
        ),
    ]
