# Generated by Django 4.2.1 on 2023-05-16 07:02

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nomi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('vacancies', models.PositiveIntegerField(default=0, verbose_name='Vakansiyalar')),
                ('status', models.BooleanField(default=True, verbose_name='Aktivligi')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='self_category', to='posts.category', verbose_name='Kategoriyasi')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('description', models.TextField(verbose_name="qo'shimcha malumot")),
                ('address', models.CharField(max_length=50, verbose_name='Manzil')),
                ('job_type', models.CharField(max_length=50, verbose_name='Bandlik turi')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Oylik maosh')),
                ('status', models.BooleanField(default=True, verbose_name='Aktivligi')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.category', verbose_name='Kategoriya')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.company')),
            ],
        ),
    ]
