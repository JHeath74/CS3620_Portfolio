# Generated by Django 2.2 on 2021-10-03 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hobby_Name', models.CharField(max_length=200)),
                ('Hobby_Description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Portfolio_Name', models.CharField(max_length=200)),
                ('Portfolio_Description', models.CharField(max_length=200)),
            ],
        ),
    ]