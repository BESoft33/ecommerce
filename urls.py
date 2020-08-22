from django.urls import path,include
from . import views

urlpatterns = [
    path('signup',views.signup),
    path('login', views.login),
    path('describe', views.describe),
    path('', views.commerce),

]
