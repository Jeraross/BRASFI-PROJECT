# Generated by Django 5.2.1 on 2025-05-15 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_BRASFI', '0011_topicconversa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicconversa',
            old_name='created_ate',
            new_name='created_at',
        ),
    ]
