# Generated by Django 5.0.4 on 2024-04-27 12:54

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('date_created', models.DateField(auto_created=True, auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('date_updated', models.DateField(auto_created=True, auto_now_add=True)),
                ('date_created', models.DateField(auto_created=True, auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('brand', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='app.brands')),
                ('category', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.subcategories')),
            ],
            options={
                'ordering': ['-date_created'],
                'unique_together': {('name', 'brand')},
            },
        ),
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('date_updated', models.DateTimeField(auto_created=True, auto_now=True)),
                ('date_created', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, default=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
            ],
            options={
                'ordering': ['-date_created'],
                'unique_together': {('user', 'product')},
            },
        ),
    ]
