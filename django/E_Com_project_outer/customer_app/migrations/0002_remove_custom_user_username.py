# Generated by Django 5.0.6 on 2024-09-16 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='username',
        ),
    ]