# Generated by Django 3.2.8 on 2022-02-19 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('func3api', '0022_rename_name1_all_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='all',
            old_name='name',
            new_name='name1',
        ),
    ]
