# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCreate(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_list')
    success_message = "Post creado correctamente!"