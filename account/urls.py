from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('pass_reset/', views.pass_reset, name="pass_reset"),
    path('settings/', views.settings, name="settings")
]
