# Generated by Django 4.0.5 on 2023-02-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softwares', '0007_betsitedesktop_login_button_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='betsite',
            name='login_button',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='betsite',
            name='username_input',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
