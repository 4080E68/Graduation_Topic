# Generated by Django 3.2.8 on 2022-03-06 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('func3api', '0031_cpu_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu',
            name='test',
        ),
    ]
