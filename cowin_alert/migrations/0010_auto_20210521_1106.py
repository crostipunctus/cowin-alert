# Generated by Django 3.1.1 on 2021-05-21 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowin_alert', '0009_user_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='center',
            old_name='center_slots',
            new_name='center_slots_dose1',
        ),
        migrations.AddField(
            model_name='center',
            name='center_slots_dose2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]