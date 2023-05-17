# Generated by Django 4.2.1 on 2023-05-16 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('age', models.PositiveIntegerField(verbose_name='Yosh')),
                ('about', models.TextField(blank=True, null=True, verbose_name='Shaxs haqida')),
                ('degree', models.CharField(choices=[("O'rta", "O'rta"), ("O'rta Maxsus", "O'rta Maxsus"), ('Tugallanmagan oliy', 'Tugallanmagan oliy'), ('Oliy', 'Oliy'), ('Magistr', 'Magistr')], default="O'rta Maxsus", max_length=50)),
                ('kasbi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Kasbi')),
                ('is_busy', models.BooleanField(default=False, verbose_name='Ishlaydi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sphere', models.CharField(max_length=60, verbose_name='Tajriba turi')),
                ('period', models.CharField(max_length=20, verbose_name='Tajriba muddati')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile', verbose_name='Shaxs')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='company_images/')),
                ('name', models.CharField(max_length=50, verbose_name='Kompaniya nomi')),
                ('email', models.EmailField(max_length=254, verbose_name='Email manzil')),
                ('topic', models.CharField(max_length=50, verbose_name='Faoliyat sohasi')),
                ('about', models.TextField(verbose_name='Kompaniya haqida')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Yuridik manzil (ixtiyoriy)')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=40, verbose_name='Viloyat')),
                ('district', models.CharField(max_length=40, verbose_name='Tuman/Shahar')),
                ('village', models.CharField(max_length=40, verbose_name='Qishloqcha')),
                ('street', models.CharField(max_length=40, verbose_name='Mahalla')),
                ('home', models.CharField(max_length=15, verbose_name='Uy raqami')),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile', verbose_name='Shaxs')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]