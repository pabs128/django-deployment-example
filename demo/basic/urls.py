from django.urls import path
from basic import views

app_name = 'basic'

urlpatterns = [
    path('register/',views.register,name = 'register'),
    path('login/',views.user_login,name = 'user_login'),

]