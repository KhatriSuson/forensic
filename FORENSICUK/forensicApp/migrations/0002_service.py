# Generated by Django 5.1 on 2024-09-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forensicApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='media/service')),
            ],
        ),
    ]
