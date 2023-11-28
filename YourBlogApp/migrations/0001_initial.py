# Generated by Django 4.2.7 on 2023-11-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('bio', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogID', models.IntegerField()),
                ('title', models.TextField(max_length=100)),
                ('subtitle', models.TextField(max_length=150)),
                ('context', models.TextField(max_length=450)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('editorID', models.IntegerField()),
                ('editedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
