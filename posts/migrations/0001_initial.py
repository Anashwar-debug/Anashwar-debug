# Generated by Django 5.1.1 on 2024-10-03 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('Body', models.CharField(max_length=1000000)),
                ('created_at', models.DateField(blank=True, default=datetime.datetime(2024, 10, 3, 2, 14, 6, 403113))),
            ],
        ),
    ]
