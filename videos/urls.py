
from django.urls import path
from . import views

app_name = "videos"

urlpatterns = [
    path('', views.video_list, name='list'),        # "/" -> list page
    path('new/', views.video_create, name='create'),
    path('<str:pk>/', views.video_detail, name='detail'),
    path('<str:pk>/edit/', views.video_update, name='update'),
    path('<str:pk>/delete/', views.video_delete, name='delete'),
    path('ping/', views.ping, name='ping'),
]
