from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, blank=True, default=None)
    price = models.FloatField(validators=[MinValueValidator(0.01)])

    class Meta:
        ordering = ['-date_created']
        unique_together = ('name', 'seller')
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})


class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    main_category = models.ForeignKey("Category", on_delete=models.SET_DEFAULT, null=True, default=None)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    

class PaymentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_DEFAULT, default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedbacks')
    text = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


class ProductMedia(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(null=True, verbose_name='Путь к файлу')
