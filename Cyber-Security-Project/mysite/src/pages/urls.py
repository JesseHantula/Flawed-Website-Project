from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_list/', views.create_list, name='create_list'),
    path('view_list/<int:list_id>/', views.view_list, name='view_list'),
    path('view_list/<int:list_id>/create_item/', views.create_item, name='create_item'),
    path('view_list/<int:list_id>/verify_password/', views.verify_password, name='verify_password'),
    path('complete_item/<int:item_id>/', views.complete_item, name='complete_item'),
    path('delete_list/<int:list_id>/', views.delete_list, name='delete_list'),
]