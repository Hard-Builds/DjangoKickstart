from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView

from blog.enum import PostStatusEnum
from blog.models import Post


def about_view(request):
    return render(
        request=request,
        template_name="blog/about.html",
        context={
            "title": "About ME !!!"
        }
    )


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.published()


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        if user.pk == self.request.user.pk:
            return Post.objects.filter(author=user).order_by("date_posted")
        else:
            return Post.objects.filter(author=user, status=PostStatusEnum.PUBLISHED.value).order_by("date_posted")


class DetailedPostView(DetailView):
    model = Post
    context_object_name = 'post'


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content", "status"]

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/blog"

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False
