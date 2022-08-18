from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-member/', views.add_member, name='add-member'),
    path('add-member/create-member/', views.create_member, name='create-member')
]
