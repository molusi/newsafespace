# Generated by Django 4.1.4 on 2023-07-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_vote_downvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='upvote',
            field=models.IntegerField(default=1),
        ),
    ]
