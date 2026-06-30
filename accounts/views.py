from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate


# ------------------------
# REGISTER VIEW
# ------------------------
def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # ❌ VALIDATION
        if not username or not password:
            messages.error(request, "Username and password are required")
            return redirect("register")

        # ❌ CHECK DUPLICATE USERNAME
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Try another one.")
            return redirect("register")

        # ✅ CREATE USER
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "accounts/register.html")


# ------------------------
# LOGIN VIEW
# ------------------------
def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "accounts/login.html")