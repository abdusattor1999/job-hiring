# Generated by Django 4.2.1 on 2023-05-16 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=20, verbose_name='Telefon'),
            preserve_default=False,
        ),
    ]
