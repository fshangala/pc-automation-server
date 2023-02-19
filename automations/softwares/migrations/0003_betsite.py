# Generated by Django 4.0.5 on 2023-02-17 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softwares', '0002_rename_sfname_software_repositoryname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('bet_buttons', models.CharField(max_length=200)),
                ('input_elements', models.CharField(max_length=200)),
                ('odds_input', models.IntegerField()),
                ('stake_input', models.IntegerField()),
                ('betslip_buttons', models.CharField(max_length=200)),
                ('confirm_button', models.IntegerField()),
            ],
        ),
    ]
