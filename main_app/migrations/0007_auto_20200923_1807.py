# Generated by Django 3.0.8 on 2020-09-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200922_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.CharField(choices=[('Watch', 'Watch Something'), ('Read', 'Read Something'), ('Fitness', 'Something Active'), ('Play', 'Play Something')], max_length=100),
        ),
    ]
