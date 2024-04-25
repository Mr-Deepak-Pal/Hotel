from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hotel, name='hotel'),
    path('post/', views.post_data, name='post_data'),
    path('update_hotel/<id>/', views.update_hotel, name='update_hotel'),
    path('delete_hotel/<id>/', views.delete_hotel, name='delete_hotel'),
    path('update_hotel_data/<id>/', views.update_hotel_data, name='update_hotel_data'),   
]