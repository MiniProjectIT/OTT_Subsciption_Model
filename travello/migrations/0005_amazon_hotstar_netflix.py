# Generated by Django 3.2.9 on 2022-09-08 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_ott_plans_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='amazon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('images', models.ImageField(upload_to='amazon')),
                ('ratings', models.CharField(default='', max_length=100)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('updatedTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='hotstar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('images', models.ImageField(upload_to='hotstar')),
                ('ratings', models.CharField(default='', max_length=100)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('updatedTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='netflix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('images', models.ImageField(upload_to='netflix')),
                ('ratings', models.CharField(default='', max_length=100)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('updatedTime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
