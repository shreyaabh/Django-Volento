# Generated by Django 3.2.9 on 2022-10-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20221006_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsponser',
            name='logo',
            field=models.ImageField(default=1, upload_to='sponser/'),
            preserve_default=False,
        ),
    ]
