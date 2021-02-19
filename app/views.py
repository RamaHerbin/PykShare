from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from app.form import CreateUserForm, CreateCommentForm, CreatePostForm
from app.models import Comment, Post


class Home(TemplateView):
    template_name = 'app/home.html'


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
        # form = CreateUserForm()
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
    template_name = 'app/post_list.html'


# View to create a post
@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'app/add_post.html'
    success_url = reverse_lazy('feed')

    # fields = '__all__'

    def form_valid(self, form):
        #               model                 django
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    # form_class =
    template_name = 'app/update_post.html'
    success_url = reverse_lazy('feed')
    fields = ['title', 'image']

@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    template_name = 'app/delete_post.html'
    success_url = reverse_lazy('feed')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class AddCommentView(CreateView):
    model = Comment
    form_class = CreateCommentForm
    template_name = 'app/add_comment.html'
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        #               model                 django
        form.instance.id_user = self.request.user
        form.instance.id_post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CommentDelete(DeleteView):
    model = Comment
    template_name = 'app/delete_comment.html'
    success_url = reverse_lazy('feed')


def AddLike(request, pk):
    # On prend le button avec name="post_id" (l.16 post_list.html)
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('feed'))
