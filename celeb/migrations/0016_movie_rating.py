# Generated by Django 5.0.1 on 2024-01-31 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celeb', '0015_rename_celebrity_celeb'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
