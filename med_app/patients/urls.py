from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name="signup"),
    path('patients/', views.patients, name='patients'),
    path('patients/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing')
]
