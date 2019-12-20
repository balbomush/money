from django.urls import path

from MoneyExchange import views

urlpatterns = [
    path('', views.post, name='post'),
    path('changeto/', views.changeto, name='changeto'),
]