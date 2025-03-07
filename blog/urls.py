from django.urls import path

from blog.views import about_view, PostListView, DetailedPostView, AddPostView, \
    UpdatePostView, DeletePostView

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", DetailedPostView.as_view(), name="blog-details"),
    path("post/new/", AddPostView.as_view(), name="blog-create"),
    path("post/<int:pk>/update/", UpdatePostView.as_view(),
         name="blog-update"),
    path("post/<int:pk>/delete/", DeletePostView.as_view(),
         name="blog-delete"),
    path("about/", about_view, name="blog-about")
]
