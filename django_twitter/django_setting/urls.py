from django.urls import path
from . import views

urlpatterns = [
    path('', views.setting, name='setting'),
    path('change_username/',views.change_username, name='change_username'),
    path('change_email/', views.change_email, name='change_email'),
    path('change_mobile-number/', views.change_mobile_number, name='change_mobile_number'),
    path("change_password",views.PasswordReset.as_view(),name="request-password-reset",),
    path("password-reset/<str:encoded_pk>/<str:token>/", views.ResetPasswordAPI.as_view(),
         name="reset-password", ),
]
