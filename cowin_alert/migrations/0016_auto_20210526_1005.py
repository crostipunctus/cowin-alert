# Generated by Django 3.1.1 on 2021-05-26 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cowin_alert', '0015_center_session_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='center',
            name='center_slots_dose1',
        ),
        migrations.RemoveField(
            model_name='center',
            name='center_slots_dose2',
        ),
        migrations.RemoveField(
            model_name='center',
            name='session_id',
        ),
        migrations.CreateModel(
            name='Slots_dose2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slots', models.IntegerField(blank=True, default=0)),
                ('center_slots', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cowin_alert.center')),
            ],
        ),
        migrations.CreateModel(
            name='Slots_dose1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slots', models.IntegerField(blank=True, default=0)),
                ('center_slots', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cowin_alert.center')),
            ],
        ),
        migrations.CreateModel(
            name='Session_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.TextField(max_length=100)),
                ('center_session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cowin_alert.center')),
            ],
        ),
    ]
