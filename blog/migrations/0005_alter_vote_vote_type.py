# Generated by Django 4.1.4 on 2023-07-17 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_type',
            field=models.IntegerField(default=0),
        ),
    ]
