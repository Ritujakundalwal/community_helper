
from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('request-help/', views.request_help, name='request_help'),
    path('view-requests/', views.view_requests, name='view_requests'),
    path('accept/<int:pk>/', views.accept_request, name='accept_request'),
    path('profile/', views.profile, name='profile'), 
    path('top_helpers/', views.top_helpers, name='top_helpers'),
]
