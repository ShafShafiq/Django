from django.urls import path
from django.contrib.auth.views import LogoutView


from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authorize' , views.AuthorizeView.as_view()),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup')

]