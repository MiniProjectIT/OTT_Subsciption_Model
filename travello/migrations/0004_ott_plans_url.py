# Generated by Django 3.2.9 on 2022-09-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_auto_20220904_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='ott_plans',
            name='url',
            field=models.CharField(default='', max_length=200, unique=True, verbose_name="URL (auto generated. Don't touch)"),
        ),
    ]