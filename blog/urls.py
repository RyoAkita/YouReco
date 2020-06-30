from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('comment/<int:post_pk>/', views.CommentView.as_view(), name='comment'),
    path('share/', views.ShareView.as_view(), name='share'),
    path('create/', views.create_account, name='create_account'),
    path('login/', views.account_login , name='login'),
    path('logout/', LogoutView.as_view(), {'template_name': 'base.html'}, name='logout'),
    path('about/', views.about_view, name='about')
]