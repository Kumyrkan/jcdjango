from django.db import models

class Payment(models.Model):
    TITLE_CHOICES = (
        ('cash', 'наличные'),
        ('card', 'карта')
    )

    title = models.CharField(max_length = 255, verbose_name = 'Оплата', choices = TITLE_CHOICES)

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self) -> str:
        return self.title

class Order(models.Model):
    payment = models.ForeignKey(Payment, verbose_name = 'Оплата', null = True, blank = True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255, verbose_name = 'Заказы')
    num_ord = models.IntegerField(default = 0, verbose_name = 'Номер заказа')
    price = models.IntegerField(default = 0, verbose_name = 'Цена')


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return self.title

# Create your models here.
