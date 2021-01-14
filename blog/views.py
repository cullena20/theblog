from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})


# you may get content from a database something like this and then put it in html code !
# post_ = [
#     {
#         'author': 'Cullen Anderson',
#         'title': 'Hello World',
#         'content': 'Hello world! My name is Cullen!',
#         'date': 'December 12 2020'
#     },
#     {
#         'author': 'Patrick Yu',
#         'title': 'Chess',
#         'content': 'Chess is a very cool game. You should play it!',
#         'date': 'December 12 2020'
#     },
#     {
#         'author': 'Daniel Klyevanov',
#         'title': 'Gym',
#         'content': 'Bench! Squat! Deadlift! Repeat!',
#         'date': 'December 13 2020'
#     },
#     {
#         'author': 'Nathaneil Aronov',
#         'title': 'Gym',
#         'content': 'Bench! Squat! Deadlift! Repeat!',
#         'date': 'December 13 2020'
#     },
#     {
#         'author': 'Danielle Arabova',
#         'title': 'Dan',
#         'content': 'I am Dan and I am an egg :)',
#         'date': 'December 13 2020'
#     },
#     {
#         'author': 'Isadora Rooney',
#         'title': 'Camera',
#         'content': 'I have a camera. Sex.',
#         'date': 'December 13 2020'
#     },
#     {
#         'author': 'Ellis Rubin',
#         'title': 'To Be Or...',
#         'content': 'To be... or not... to be? Such stuff as dreams are made of.',
#         'date': 'December 13 2020'
#     },
#     {
#         'author': 'Nicole Akilov',
#         'title': 'Rawr',
#         'content': 'You heard that right.',
#         'date': 'December 13 2020'
#     }
# ]
