from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Category, Comment
from django.db.models import Q
from .forms import CommentCreateForm, PostCreateForm, UserCreateForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

class IndexView(generic.ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self):
        queryset =  Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
                )
        
        return queryset

class CategoryView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-created_at').filter(category=category)
        return queryset

class DetailView(generic.DetailView):
    model = Post

class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def get_initial(self):
        username = self.request.user
        initial = super().get_initial()
        initial["name"] = username
        return initial

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('blog:detail', pk=post_pk)

class ShareView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:index')

class Create_account(generic.CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'create.html', {'form': form,})
    
create_account = Create_account.as_view()

class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form,})

account_login = Account_login.as_view()

class AboutView(TemplateView):
    template_name = 'blog/about.html'

about_view = AboutView.as_view()


