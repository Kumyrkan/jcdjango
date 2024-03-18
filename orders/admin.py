from django.contrib import admin
from django.utils.html import mark_safe
from orders.models import Order, Payment

# admin.site.register(Order)
admin.site.register(Payment)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets=(
    ('Наименование',{'fields':('title',)}),
    ('О заказе',{'fields':('num_ord','price')}),
    ('Способ оплаты',{'fields':('payment',)})
    )
    # fields=('title','price','num_ord','payment')
    list_display=('title','num_ord','price')
    list_filter=('num_ord','price')
    search_fields=('title',)
 