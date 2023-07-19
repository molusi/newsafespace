# Generated by Django 4.1.4 on 2023-07-17 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_article_votes_article_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(blank=True, default='https://www.linkedin.com/in/abigail-molusi-a8719b229/?originalSubdomain=za', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(blank=True, default='https://twitter.com/AbigailMolusi', null=True),
        ),
    ]
