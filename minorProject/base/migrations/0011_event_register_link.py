# Generated by Django 3.2.4 on 2023-06-15 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='register_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]