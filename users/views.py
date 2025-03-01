from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import UserRegisterForm


@login_required
def profile(request):
    return render(request, "users/profile.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request=request,
                message=f"Your account has been created!"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
    )
