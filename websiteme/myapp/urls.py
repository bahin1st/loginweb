from django.urls import path
from .views import register,housecliked,login_view,logout_view,main_view,some_view,clear_session_data,profile,house_list,register_house,edit_house
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
   path('login/coming/',main_view, name='home'),
    path('coming/',main_view, name='home'),
    path('data/',some_view,name='set_session'),
     path('clear_session/',clear_session_data, name='clear_session'),
    path('profile/', profile, name='profile'),
     path('register_house/', register_house, name='register_house'),
    path('house_list/', house_list, name='house_list'),
     path('edit_house/<int:house_id>/', edit_house, name='edit_house'),
    path('house_list/house/<int:id>/',housecliked, name='housedetail')
]
