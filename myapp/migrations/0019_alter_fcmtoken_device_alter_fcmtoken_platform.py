# Generated by Django 5.1.1 on 2024-11-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_fcmtoken_device_alter_fcmtoken_fcm_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcmtoken',
            name='device',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='fcmtoken',
            name='platform',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
