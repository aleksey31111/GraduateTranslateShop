from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название Устройства')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')

    class Meta:
        # ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категоря')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название Устройства')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение Устройства')
    description = models.TextField(blank=True, verbose_name='Описание')
    short_description = models.CharField(max_length=300, blank=True, verbose_name="Краткое описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Количество')
    available = models.BooleanField(default=True, verbose_name='Есть в наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавление')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновление')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        # ordering = ['-time']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail',
                       args=[self.id, self.slug])
