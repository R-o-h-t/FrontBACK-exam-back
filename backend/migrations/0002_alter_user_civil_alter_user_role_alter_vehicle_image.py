# Generated by Django 4.1.2 on 2022-11-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='civil',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('A', 'Admin'), ('U', 'User')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
