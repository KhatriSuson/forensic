# Generated by Django 5.1 on 2024-09-29 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forensicApp', '0011_delete_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
