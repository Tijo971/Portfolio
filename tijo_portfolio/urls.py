from django.urls import path

from tijo_portfolio import views


urlpatterns=[
    path('', views.index, name='index'),
    
]