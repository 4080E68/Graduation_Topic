# Generated by Django 3.2.8 on 2022-03-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func3api', '0038_auto_20220316_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='HDD1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=3000)),
                ('url_list', models.CharField(default='', max_length=3000)),
                ('pc_images', models.CharField(default='', max_length=3000)),
                ('capacity_TB', models.FloatField(default='0.0', max_length=100)),
                ('size', models.CharField(default='', max_length=100)),
                ('Rotating_speed', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
