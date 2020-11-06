from django.urls import path
from .views import signup
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/',signup,name="signup"),
    #path('login/',views.login,name="login")
    path('login/', auth_views.LoginView.as_view(template_name='Account/Login.html'), name='login')
]
