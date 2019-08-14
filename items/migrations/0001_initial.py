# Generated by Django 2.2.3 on 2019-07-26 14:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=15)),
                ('price', models.CharField(default='', max_length=20)),
                ('year', models.CharField(default='', max_length=20)),
                ('imgs', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('favs', models.IntegerField(default=0)),
            ],
        ),
    ]
