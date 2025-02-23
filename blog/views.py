from django.shortcuts import render

from blog.models import Post


def home_view(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(
        request=request,
        template_name="blog/home.html",
        context=context
    )


def about_view(request):
    return render(
        request=request,
        template_name="blog/about.html",
        context={
            "title": "About ME !!!"
        }
    )
