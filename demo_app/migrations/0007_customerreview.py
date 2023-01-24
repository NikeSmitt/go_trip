# Generated by Django 4.1.3 on 2022-12-15 18:01

import demo_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0006_villa_is_recommended'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=50, null=True)),
                ('body', models.CharField(max_length=500)),
                ('avatar', models.ImageField(null=True, upload_to=demo_app.models.get_upload_path)),
            ],
        ),
    ]