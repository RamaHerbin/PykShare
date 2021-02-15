from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView

from app.form import CreateUserForm
from app.models import Comment, Person, Like, Picture, Post


class RegisterPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('feed')
        else:
            form = CreateUserForm()
            return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = CreateUserForm()
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))
        form = CreateUserForm()
        return render(request, 'accounts/register.html', {'form': form})


class LoginPage(View):
    # if request.user.is_authenticated:
    #     return redirect('feed')
    # else:
    def get(self, request):
        return render(request, 'accounts/login.html', {'form': AuthenticationForm})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            messages.info(request, 'Username ou password incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@method_decorator(login_required, name='dispatch')
class PostList(ListView):
    model = Post


# View to create a post
@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    success_url = 'feed/'
    fields = ['picture', 'uploaded_at']

    def form_valid(self, form):
        form.instance.person_id = self.kwargs.get('pk')
        return super(PostCreate, self).form_valid(form)
