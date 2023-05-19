from django.urls import path
from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/weight_track', views.weight_track, name='weight_track'),
    path('update_weight', views.update_weight, name='update_weight'),
]