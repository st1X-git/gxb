from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # path(r'^login$', views.login.as_view(template_name='users/login.html')),
    # path('logout', views.logout, name='logout'),


]
