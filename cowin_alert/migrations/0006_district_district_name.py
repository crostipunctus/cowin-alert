# Generated by Django 3.1.1 on 2021-05-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowin_alert', '0005_auto_20210521_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='district_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]