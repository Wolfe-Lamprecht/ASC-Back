# Generated by Django 3.1.7 on 2021-03-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asc', '0002_auto_20210307_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(upload_to='asc_django/profile_pics'),
        ),
    ]