from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    preview_image = models.FileField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, blank=True, default=None, related_name='products')
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


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
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
    main_category = models.ForeignKey(
        "Category", 
        on_delete=models.SET_DEFAULT, 
        null=True, 
        default=None,
        blank=True,
        related_name='subcategories'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='orders')
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_DEFAULT, default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return f"Заказ №{self.id}"


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Часть заказа'
        verbose_name_plural = 'Части заказа'


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
