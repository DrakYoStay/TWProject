from django.urls import path
from fintess_app import views

app_name = 'fintess_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('sign_up/', views.signup_view, name='sign_up'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
