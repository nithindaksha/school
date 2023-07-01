from django.urls import path

from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('form',views.form,name='form'),
    path('cs',views.cs,name='cs'),
    path('add',views.add,name='add'),

    path('logout',views.logout,name='logout'),
]