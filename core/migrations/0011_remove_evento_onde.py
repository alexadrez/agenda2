# Generated by Django 3.2.7 on 2021-09-22 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_evento_local'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='onde',
        ),
    ]
