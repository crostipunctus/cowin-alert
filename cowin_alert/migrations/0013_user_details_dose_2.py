# Generated by Django 3.1.1 on 2021-05-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowin_alert', '0012_auto_20210521_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='dose_2',
            field=models.BooleanField(default=False),
        ),
    ]
