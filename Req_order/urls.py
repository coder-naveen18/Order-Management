from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.listdisplay, name='display-list'),
    path('request/', views.request_order_view , name='request-view'),
    path('success/', views.success_page, name = 'success-page'),
    path('<int:ord_id>/fulfilled/', views.order_fulfilled, name="order-fulfilled"),
    
]