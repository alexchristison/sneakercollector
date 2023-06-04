from django.urls import path
from . import views 
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sneakers/', views.sneakers_index, name='index'), # can also be name='sneakers_index' BUT doesn't have to be
    path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name='detail'),
    path('sneakers/create/', views.SneakerCreate.as_view(), 
         name='sneakers_create'),
    path('sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneakers_update'),
    path('sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneakers_delete'),
    path('sneakers/<int:sneaker_id>/add_worn/', views.add_worn, name='add_worn'),
    path('socks/', views.SockList.as_view(), name='socks_index'),
    path('socks/<int:pk>/', views.SockDetail.as_view(), name='socks_detail'),
    path('socks/create/', views.SockCreate.as_view(), name='socks_create'),
    path('socks/<int:pk>/update/', views.SockUpdate.as_view(), name='socks_update'),
    path('socks/<int:pk>/delete/', views.SockDelete.as_view(), name='socks_delete'),
]