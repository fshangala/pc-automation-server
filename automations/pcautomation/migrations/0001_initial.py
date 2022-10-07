# Generated by Django 4.0.5 on 2022-10-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devicetype', models.CharField(max_length=200)),
                ('channel', models.CharField(max_length=200, unique=True)),
                ('datetime', models.CharField(max_length=200)),
            ],
        ),
    ]
