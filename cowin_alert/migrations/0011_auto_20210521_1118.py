# Generated by Django 3.1.1 on 2021-05-21 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowin_alert', '0010_auto_20210521_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='center_slots_dose2',
            field=models.IntegerField(blank=True),
        ),
    ]