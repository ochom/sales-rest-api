# Generated by Django 3.0.2 on 2020-01-27 15:12

from django.db import migrations, models
import sales.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100, unique=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=255)),
                ('password', models.TextField(default='')),
                ('rating', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='AgentSkillModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.CharField(default='', max_length=100, unique=True)),
                ('skill', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100, unique=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=255)),
                ('password', models.TextField(default='')),
                ('location', models.CharField(default='0,0', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField(default=0)),
                ('agent_id', models.IntegerField(default=0)),
                ('product_id', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('total_cost', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='placed', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=100, unique=True)),
                ('description', models.TextField(default='')),
                ('price', models.IntegerField(default=0)),
                ('image', models.FileField(blank=True, default='', null=True, upload_to=sales.models.scramble_uploaded_filename, verbose_name='Image upload')),
                ('units', models.TextField(default='')),
            ],
        ),
    ]
