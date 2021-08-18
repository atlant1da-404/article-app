from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *


urlpatterns = [
    #CRUD
    path('', PostBaseView.as_view(), name='home'),
    path('create-post/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('update-post/<int:pk>/', PostUpdateView.as_view(), name='update-post'),
    path('delete-post/<int:pk>/', PostDeleteView.as_view(), name='delete-post'),

    #AUTH
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]