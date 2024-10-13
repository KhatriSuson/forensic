# Generated by Django 5.1 on 2024-10-13 17:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forensicApp', '0014_newsletter_subscriber_blogpost_comment_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='subscribed',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='subscribed_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
