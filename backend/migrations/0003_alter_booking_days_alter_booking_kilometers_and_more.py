# Generated by Django 4.1.2 on 2022-11-25 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_user_civil_alter_user_role_alter_vehicle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='kilometers',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
