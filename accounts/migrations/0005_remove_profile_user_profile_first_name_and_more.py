# Generated by Django 4.2.1 on 2023-05-16 17:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='default', max_length=50, verbose_name='Ism'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Familiya'),
            preserve_default=False,
        ),
    ]