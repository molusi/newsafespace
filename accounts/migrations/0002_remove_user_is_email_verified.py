# Generated by Django 4.1.4 on 2023-07-29 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_email_verified',
        ),
    ]
