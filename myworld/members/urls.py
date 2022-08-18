from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-member/', views.add_member, name='add-member'),
    path('add-member/create-member/', views.create_member, name='create-member'),
    path('delete/<int:id>', views.delete_member, name='delete-member'),
    path('update/<int:id>', views.update_member, name='update-member'),
    path('update/update-member/<int:id>', views.save_member, name='update-member')
]
