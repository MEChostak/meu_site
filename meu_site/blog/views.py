from django.db.models.fields import Field
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from . models import Post


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    #fields = '__all__'
    fields = ('title','content','author',)

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    #fields = '__all__'
    fields = ('title','content','author',)
    