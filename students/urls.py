from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_students, name='list'),
    path('add/', views.add_student, name='add'),
    path('details/<int:id>/', views.student_detail, name='details'),
    path('edit/<int:id>/', views.edit_student, name='edit'),
    path('delete/<int:id>/', views.delete_student, name='delete')
]