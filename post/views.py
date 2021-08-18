from django.urls import reverse_lazy

from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView, 
    DeleteView, FormView )

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

from .models import News


class PostBaseView(ListView):
    """Получение всех записей на 'endpoint' '/' ."""

    model = News
    context_object_name = 'news'


class PostDetailView(DetailView):
    """Получение *1* детальной записи на 'endpoint' 'post/<int:pk>/' ."""

    model = News
    context_object_name = 'news'


class PostCreateView(CreateView):
    """Создание *1* записи на 'endpoint' 'create-post/' ."""

    model = News
    fields = '__all__'
    success_url = reverse_lazy('home') # Переадресация на главную страничку


class PostUpdateView(UpdateView):
    """Обновление *1* записи на 'endpoint' 'update-post/' ."""

    model = News
    fields = '__all__'
    success_url = reverse_lazy('home') # Переадресация на главную страничку


class PostDeleteView(DeleteView):
    """Удаление *1* записи на 'endpoint' 'delete-post/' ."""

    model = News
    context_object_name = 'news'
    success_url = reverse_lazy('home') # Переадресация на главную страничку


class UserLoginView(LoginView):
    """Авторизация пользователя"""

    template_name = 'post/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('home')  # Переадресация на главную страничку


class UserRegisterView(FormView):
    """Регистрация пользователя"""

    template_name = 'post/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home') # Переадресация на главную страничку

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home') # Переадресация на главную страничку
        return super(UserRegisterView, self).get(self)
    

