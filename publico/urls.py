from django.urls import path
from .views import loginview, logoutview
from django.contrib.auth import views as auth_views

app_name="publico"
urlpatterns = [
                  path('login', loginview, name="login"),
                  path('logout', logoutview, name="logout"),

                 # path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),
              
              ] 