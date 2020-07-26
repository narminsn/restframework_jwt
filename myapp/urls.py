from django.urls import path
# from .views import RegisterApi
# from .views import register_view, login_view, logout_view,\
from .views import  UserName, RegisterApi

urlpatterns = [

    path('registerapi/', RegisterApi.as_view(), name="register-api"),
    # path('register/', register_view, name='register'),
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),

    path('user/', UserName.as_view(), name="username"),
    # path('private/', PrivateApi.as_view(), name="PrivateApi"),
    # path('login/', LoginApi.as_view(), name="login-api"),

]