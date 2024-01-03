from api import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('task-list/', views.taskList, name='task-List'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
]