from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect


def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # 🔴 CHECK IF USER EXISTS
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Try another one.")
            return redirect("register")

        # 🔴 CREATE USER SAFELY
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "accounts/register.html")