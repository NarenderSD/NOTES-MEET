"""
URL configuration for notessharing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.Index, name='index'),
    path('Notes', views.NOTES_DETAILS, name='notes_details'),
    path('Dashboard', views.DASHBOARD, name='dashboard'),
    path('Login', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    path('usersignup/', views.USERSIGNUP, name='usersignup'),
    path('Profile', views.PROFILE, name='profile'),
    path('Password', views.CHANGE_PASSWORD, name='change_password'),
    path('AddNotes', views.ADD_NOTES, name='add_notes'),
    path('ManageNotes', views.MANAGE_NOTES, name='manage_notes'),
    path('DeleteNOTES/<str:id>', views.DELETE_NOTES, name='delete_notes'),
     path('ViewNotes/<str:id>', views.VIEW_NOTES, name='view_notes'),
     path('EditNotes', views.EDIT_NOTES, name='edit_notes'),
   path('SearchNotes', views.SEARCH_NOTES, name='search_notes'),
   
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
