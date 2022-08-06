from django.urls import path
from .views import *

app_name = 'book_site'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', Login_user, name='login'),
    path('logout/', Logout, name='logout'),
    path('profile/<user_id>', profileUser, name='profile'),
    path('shop/<int:id>', shopingView, name='shop'),
    path('shoping-cart/', shopingCart, name='shop-cart'),

]