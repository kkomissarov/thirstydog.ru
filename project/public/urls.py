from django.urls import path
from .views import MainPage, ProductPage, CategoryPage, InfoPage, SubscribeView, OrderView


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('category/<slug>/', CategoryPage.as_view(), name='category_page'),
    path('product/<slug>/', ProductPage.as_view(), name='product_page'),
    path('info/<slug>/', InfoPage.as_view(), name='info_page'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe_view'),
    path('create-order/', OrderView.as_view(), name='order_view'),
]

