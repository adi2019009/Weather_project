# here we are import path from in-built django-urls
from django.urls import path
from weatherupdates.views import index, login
from .views import signup,logout

# here we are importing all the Views from the views.py file
from .import views

urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
   
]