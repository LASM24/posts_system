# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
