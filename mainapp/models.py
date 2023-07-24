from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Пользователи"""
    patronymic = models.CharField('Отчество', max_length=50, null=True, blank=True)
    phone = models.CharField('Номер телефона', max_length=11)

    def __str__(self):
        return str(self.username)


class Category(models.Model):
    """Категории работ"""
    name_category = models.CharField(max_length=100, verbose_name='Категория')
    category_view = models.CharField(max_length=100, default="checkbox", verbose_name='Тип категории')

    def __str__(self):
        return str(self.name_category)


class TypeWork(models.Model):
    """Виды работ"""
    name_work = models.CharField(max_length=100, verbose_name='Название работы')
    work_descrip = models.TextField(verbose_name='Описание работы')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    hours = models.IntegerField(verbose_name='Трудозатраты')
    price = models.IntegerField(verbose_name='Стоимость нормо-часа')
    cost = models.IntegerField(blank=True, null=True, verbose_name='Итоговая стоимость')

    def __str__(self):
        return self.name_work

    def save(self, *args, **kwargs):
        self.cost = self.hours * self.price
        super(TypeWork, self).save(*args, **kwargs)

class Order(models.Model):
    """Заказы"""
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id пользователя')


class OrderWork(models.Model):
    """Работы заказа"""
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    id_work = models.ForeignKey(TypeWork, on_delete=models.CASCADE, verbose_name='Работа')
