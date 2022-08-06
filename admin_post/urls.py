from django.urls import path
from .views import *
app_name = "admin_post"
urlpatterns = [
    path('', books, name='books'),
    path('title/<slug:slug>/<int:id>/', bookDetail, name='Detail'),
    path('category/<slug:slug>/', categorys, name='Category'),
    path('commentposts/<int:id>/', comments, name='comments'),
]