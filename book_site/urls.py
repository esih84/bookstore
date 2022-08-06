from django.urls import path
from .views import Login_user, signup, Logout, profileUser

app_name = 'book_site'

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', Login_user, name='login'),
    path('logout/', Logout, name='logout'),
    path('profile/<user_id>', profileUser, name='profile'),
]