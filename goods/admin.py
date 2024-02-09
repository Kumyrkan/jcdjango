from django.contrib import admin
from goods.models import Good, Category, Review

admin.site.register(Category)
admin.site.register(Good)
admin.site.register(Review)

# Register your models here.
