# Generated by Django 5.1.1 on 2024-11-13 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_termsandconditions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termsandconditions',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
