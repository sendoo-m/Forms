# Generated by Django 3.2 on 2022-11-03 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_candidate_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='situation',
            field=models.CharField(choices=[('pending', 'pending'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='pending', max_length=50, null=True),
        ),
    ]
