# Generated by Django 3.2.8 on 2022-03-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func3api', '0033_auto_20220315_2044'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='hdd',
            name='capacity_TB',
            field=models.FloatField(default='0.0', max_length=100),
        ),
        migrations.AlterField(
            model_name='ssd',
            name='capacity_TB',
            field=models.FloatField(default='0.0', max_length=100),
        ),
    ]
