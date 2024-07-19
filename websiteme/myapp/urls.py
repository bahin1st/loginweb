from django.urls import path
from .views import register,housecliked,login_view,logout_view,main_view,profile,house_list,register_house,edit_house,property_delete
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', house_list, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
     path('register_house/', register_house, name='register_house'),
    path('house_list/', house_list, name='house_list'),
     path('edit_house/<int:house_id>/', edit_house, name='edit_house'),
    path('house_list/house/<int:id>/',housecliked, name='housedetail'),
    path('house/<int:id>/',housecliked, name='housedetail'),
    path('house/<int:pk>/delete/',property_delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
