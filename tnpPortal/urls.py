from django.contrib import admin
from django.urls import path, include, re_path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('tnp/', views.home, name='ho'),
    path('signup', views.signup, name='signup'),
    
    path('login', views.login, name='login'),

    path('dash', views.dash, name='dash'),
    path('profile', views.profile, name='profile'),
    #path('profile', views.test, name='profile'),
    path('logout', views.logOut, name='logout'),
    path('admin/addcompany/logout', views.logOut, name='logout'),
    
    path('changepassword', views.changepass, name='changepass'),
    path('changeProfile', views.changeProfile, name='changeProfile'),

    path('student/<int:id>/', views.profile, name='studdata'),


    path('admin/addcompany/', views.companydata, name='addcompany'),

    re_path(r'^''comp/(?P<slug>[\w@.-]+)', views.comp, name='comp'),
]