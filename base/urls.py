from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login_page/',views.loginPage,name="login"),
    path('register_page/',views.registerUser,name="register"),
    path('logout/',views.logOutUser,name="logout"),
    path('room_page/<str:pk>/',views.room,name="room"),
    path('create_room/',views.createRoom,name="create_room"),
    path('update_room/<str:pk>',views.updateRoom,name="update_room"),
    path('delete_room/<str:pk>',views.deleteRoom,name="delete_room"),
    path('delete_message/<str:pk>',views.deleteMessage,name="delete_message")
    

]