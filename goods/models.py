from django.db import models


class Category(models.Model):
    title = models.CharField('Наименование категории', max_length = 255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title

class Good(models.Model):
    COLORS_CHOICES = (
        ('red', 'Красное'),
        ('white', 'Белое')
    )

    image = models.ImageField(verbose_name = 'Изображение')
    category = models.ForeignKey(Category, verbose_name = 'Категория', null = True, blank = True, on_delete = models.CASCADE)
    color = models.CharField(verbose_name = 'Цвет', choices = COLORS_CHOICES, max_length = 255, default = 'red')
    title = models.CharField(max_length = 255, verbose_name = 'Заголовок')
    price = models.IntegerField(default = 0, verbose_name = 'Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self) -> str:
        return self.title
    

class Review(models.Model):
    RATE_CHOICES = (
        ('5','5'),
        ('4','4'),
        ('3','3'),
        ('2','2'),
        ('1','1'),
        ('0','0'),
    )

    rate = models.IntegerField(verbose_name = 'Оценка',choices = RATE_CHOICES, default = 5)
    text = models.TextField(verbose_name = 'Отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self) -> str:
        return self.text

# Create your models here.
