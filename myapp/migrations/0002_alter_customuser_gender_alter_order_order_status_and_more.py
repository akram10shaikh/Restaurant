# Generated by Django 5.1.1 on 2024-10-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('male', 'Female'), ('other', 'Other')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('ongoing', 'Ongoing'), ('order ready', 'Order ready'), ('completed', 'Completed')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='tag',
            field=models.CharField(choices=[('delivered', 'Delivered'), ('not delivered', 'Not Delivered'), ('pickup', 'Pickup'), ('order', 'Order')], max_length=255, null=True),
        ),
    ]
