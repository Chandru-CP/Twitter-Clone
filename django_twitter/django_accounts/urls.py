from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.signin_view, name='login'),
    path('signout/', views.sign_out, name='signout'),
    path('', views.dashboard, name='dashboard')
]