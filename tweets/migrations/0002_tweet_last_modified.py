# Generated by Django 4.1.6 on 2023-02-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]