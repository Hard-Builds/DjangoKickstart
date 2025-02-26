from django.contrib import messages
from django.shortcuts import render, redirect

from users.forms import UserRegisterForm


def user_home(request):
    return redirect("user-reg")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request=request,
                message=f"User {username} registered successfully!!!"
            )
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
    )
