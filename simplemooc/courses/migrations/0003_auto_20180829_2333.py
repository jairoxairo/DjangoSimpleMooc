# Generated by Django 2.1 on 2018-08-30 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180828_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='created_ate',
            new_name='created_at',
        ),
    ]