# Generated by Django 3.2.8 on 2022-06-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name_all', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=255)),
                ('url_list', models.CharField(default='', max_length=255)),
                ('pc_images', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=255)),
                ('url_list', models.CharField(default='', max_length=255)),
                ('pc_images', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='chassis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=255)),
                ('url_list', models.CharField(default='', max_length=255)),
                ('pc_images', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='cpu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=255)),
                ('url_list', models.CharField(default='', max_length=255)),
                ('pc_images', models.CharField(default='', max_length=255)),
                ('chip', models.CharField(default='', max_length=255)),
                ('thread', models.CharField(default='', max_length=255)),
                ('speed', models.CharField(default='', max_length=255)),
                ('foot_position_cpu', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('pc_images', models.CharField(default='', max_length=3000)),
                ('url_list', models.CharField(default='', max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=255)),
                ('url_list', models.CharField(default='', max_length=255)),
                ('pc_images', models.CharField(default='', max_length=255)),
                ('display_chip', models.CharField(default='', max_length=255)),
                ('Memory', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='hdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=255)),
                ('url_list', models.CharField(default='', max_length=255)),
                ('pc_images', models.CharField(default='', max_length=255)),
                ('capacity_TB', models.FloatField(default='0.0', max_length=255)),
                ('size', models.CharField(default='', max_length=255)),
                ('Rotating_speed', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='hit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(default='', max_length=255)),
                ('cpu_hit', models.IntegerField(default=0)),
                ('mb_hit', models.IntegerField(default=0)),
                ('ssd_hit', models.IntegerField(default=0)),
                ('hdd_hit', models.IntegerField(default=0)),
                ('display_hit', models.IntegerField(default=0)),
                ('memory_hit', models.IntegerField(default=0)),
                ('power_hit', models.IntegerField(default=0)),
                ('chassis_hit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=255)),
                ('url_list', models.CharField(default='', max_length=255)),
                ('pc_images', models.CharField(default='', max_length=255)),
                ('foot_position_MB', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=255)),
                ('url_list', models.CharField(default='', max_length=255)),
                ('pc_images', models.CharField(default='', max_length=255)),
                ('Memory_Specifications', models.CharField(default='', max_length=255)),
                ('capacity_GB', models.IntegerField(default='')),
                ('type', models.CharField(default='', max_length=255)),
                ('clock_rate', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=255)),
                ('url_list', models.CharField(default='', max_length=255)),
                ('pc_images', models.CharField(default='', max_length=255)),
                ('Watts', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='prs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(default='', max_length=255)),
                ('type', models.CharField(default='', max_length=255)),
                ('time', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ssd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default='')),
                ('commodity', models.CharField(default='', max_length=255)),
                ('url_list', models.CharField(default='', max_length=255)),
                ('pc_images', models.CharField(default='', max_length=255)),
                ('capacity_TB', models.FloatField(default='0.0', max_length=255)),
                ('size', models.CharField(default='', max_length=255)),
                ('read_speed_mbs', models.IntegerField(default='')),
                ('write_speed_mbs', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=255)),
                ('username', models.CharField(default='', max_length=255)),
                ('sex', models.BooleanField(default='')),
            ],
        ),
    ]
