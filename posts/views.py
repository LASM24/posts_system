# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


@method_decorator(staff_member_required, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm

    def get_success_url(self):
            return reverse_lazy('posts:posts') + '?os' 


@method_decorator(staff_member_required, name="dispatch")
class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
            return reverse_lazy('posts:posts') + '?ok' 


@method_decorator(staff_member_required, name="dispatch")
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name_suffix = "_update_form"


    def get_success_url(self):
            return reverse_lazy('posts:update', args=[self.object.id]) + '?or' 

    def form_valid(self, form):
            instance = form.save(commit=False)

            if 'image' in self.request.FILES:
                instance.image = self.request.FILES['image']

            instance.save()

            return HttpResponseRedirect(self.get_success_url())
