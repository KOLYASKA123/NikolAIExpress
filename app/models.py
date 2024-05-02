from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateField(default=timezone.now)
    date_updated = models.DateField(auto_now=True)
    brand = models.ForeignKey('Brands', on_delete=models.CASCADE)
    category = models.ForeignKey('SubCategories', on_delete=models.SET_DEFAULT, blank=True, default=1)
    price = models.FloatField(validators=[MinValueValidator(0.01)])

    class Meta:
        ordering = ['-date_created']
        unique_together = ('name', 'brand')
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})


class Brands(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    date_created = models.DateField(default=timezone.now)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    parent = models.ForeignKey('Categories', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


# class Characteristics(models.Model):
#     ...
#
#
# class Order(models.Model):
#     ...


class Feedbacks(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='feedbacks')
    text = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text
