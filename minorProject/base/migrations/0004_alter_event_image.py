# Generated by Django 3.2.4 on 2023-04-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='files/images'),
        ),
    ]