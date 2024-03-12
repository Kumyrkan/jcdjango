from django.contrib import admin
from goods.models import Good, Category, Review

admin.site.register(Category)
admin.site.register(Review)

# Register your models here.

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display=('title','category','color','price','created_at')
    list_filter=('category','color')
    search_fields=('title',)