from django.urls import path
from .views import register,login_view,logout_view,main_view,some_view,clear_session_data,profile
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
   path('login/coming/',main_view, name='home'),
    path('coming/',main_view, name='home'),
    path('data/',some_view,name='set_session'),
     path('clear_session/',clear_session_data, name='clear_session'),
    path('profile/', profile, name='profile'),

]
