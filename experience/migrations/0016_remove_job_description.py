# Generated by Django 4.2.2 on 2023-06-26 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0015_jobdescription_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='description',
        ),
    ]
