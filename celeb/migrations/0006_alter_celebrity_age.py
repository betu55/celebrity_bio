# Generated by Django 5.0.1 on 2024-01-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celeb', '0005_alter_celebrity_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebrity',
            name='age',
            field=models.IntegerField(),
        ),
    ]
