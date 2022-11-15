# Generated by Django 3.2 on 2022-11-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_auto_20221114_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='job',
            field=models.CharField(max_length=10, verbose_name='Job Code'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='message',
            field=models.TextField(verbose_name='Presentation'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='salary',
            field=models.CharField(max_length=50, verbose_name='Salary expectation'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='smoker',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='status_course',
            field=models.CharField(choices=[('', 'Select your status course'), ("i' am studying", "i' am studying"), ('I took a break', 'I took a break'), ('Complated', 'Complated')], max_length=50, null=True),
        ),
    ]
