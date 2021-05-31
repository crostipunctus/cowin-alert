# Generated by Django 3.1.1 on 2021-05-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowin_alert', '0018_auto_20210526_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='user_district',
        ),
        migrations.AddField(
            model_name='user_details',
            name='user_district',
            field=models.ManyToManyField(to='cowin_alert.District'),
        ),
    ]
