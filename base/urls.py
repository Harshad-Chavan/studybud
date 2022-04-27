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
    path('delete_message/<str:pk>',views.deleteMessage,name="delete_message"),
    path('profile/<str:pk>/',views.userProfile,name="user_profile"),
    path('update_user',views.updateUser,name="update_user"),
    path('topics',views.topicsPage,name="topics"),
    path('activites',views.activityPage,name="activites"),
    path('task',views.celery_task_demo,name="celery_task_demo")
    
    

]