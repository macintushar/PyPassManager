from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

app_name = 'PyPasswordManager'
urlpatterns = [
    path('', views.index, name='Index'),
    path('create/',views.NewPassword,name=('New Password')),
    path('delete/<uid>',views.DeletePassword,name=('Delete Password')),
    path('view-password/<uid>',views.ViewPassword, name=('View Password')),
    path('login/',views.login_user,name=('Login')),
    path('logout/', views.logout_user, name=('Logout')),
    path("register/", views.create_user, name=('register')),
]