# Generated by Django 3.2.9 on 2022-09-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_amazon_hotstar_netflix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ott_plans',
            name='f4',
        ),
        migrations.AddField(
            model_name='ott_plans',
            name='amt',
            field=models.IntegerField(default=999),
        ),
    ]
