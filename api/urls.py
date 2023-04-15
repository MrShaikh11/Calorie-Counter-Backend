from django.urls import path
from api import views

urlpatterns = [
    path('foods/', views.FoodList.as_view()),
    path('foods/<int:pk>/', views.FoodDetail.as_view()),
    path('today/', views.FoodAddedList.as_view()),
    path('today/<int:pk>/', views.FoodAddedDetail.as_view())
]
