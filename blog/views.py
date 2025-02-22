from django.shortcuts import render


def home_view(request):
    context = {
        "posts": [
            {
                "author": "Hardik",
                "title": "Blog Post 1",
                "content": "ABCD.....",
                "date_posted": "Feb 20, 2025"
            },
            {
                "author": "Hardik",
                "title": "Blog Post 2",
                "content": "WXYZ.....",
                "date_posted": "Feb 21, 2025"
            }
        ]
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
