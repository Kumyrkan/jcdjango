from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import GoodList, GoodDetail, GoodView, OrderView

router = DefaultRouter()
router.register('goods',GoodView, basename='goods')
router.register('orders',OrderView, basename='orders')

urlpatterns = [
    path('goods/', GoodList.as_view()),
    path('good/<int:pk>/', GoodDetail.as_view()),
    # path('good_view_set/', GoodView.as_view({'get':'list', 'post':'create'}))
    path('good_view_set/',include(router.urls)),
]