# Generated by Django 4.2.1 on 2023-07-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userp',
            name='address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userp',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userp',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userp',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]