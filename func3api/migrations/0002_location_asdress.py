# Generated by Django 3.2.8 on 2021-11-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func3api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='asdress',
            field=models.CharField(default=123, max_length=500),
            preserve_default=False,
        ),
    ]
