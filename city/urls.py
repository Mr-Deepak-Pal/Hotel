from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.city, name='city'),
    path('post/', views.post_data, name='post_data'),
    path('update_city/<id>/', views.update_city, name='update_city'),
    path('patch/<id>/', views.patch, name='patch'),
    path('delete_city/<id>/', views.delete_city, name='delete_city')
]