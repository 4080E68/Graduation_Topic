# Generated by Django 3.2.8 on 2022-03-16 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('func3api', '0039_hdd1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mb',
            old_name='foot_position',
            new_name='foot_position_MB',
        ),
    ]
