# Generated by Django 3.2.8 on 2021-12-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func3api', '0010_auto_20211223_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='aaa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(max_length=500)),
                ('commodity', models.CharField(max_length=3000)),
            ],
        ),
    ]
