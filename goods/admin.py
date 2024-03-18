from django.contrib import admin
from django.utils.html import mark_safe
from goods.models import Good, Category


class GoodInline(admin.TabularInline):
    model = Good
    extra=0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [GoodInline,]

# admin.site.register(Good)

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    fieldsets=(
    ('Изображение',{'fields':('image',)}),
    ('Наимеменование и категория',{'fields':('title','category')}),
    ('Остальные характеристики',{'fields':('price',)})
    )
    # fields = [('image', 'title', 'category'), 'price', 'color',]
    readonly_fields=('good_obj_image',)
    list_display=('title','category','color','price','created_at','good_list_image')
    list_filter=('category','color')
    search_fields=('title',)

    def good_list_image(self, obj):
        return mark_safe(f'<img src = "{obj.image.url}" width = 10%>')
    
    good_list_image.short_description = 'Превью'

    def good_obj_image(self, obj):
        return mark_safe(f'<img src = "{obj.image.url}" width = 10%>')
    
    good_obj_image.short_description = 'Превью'