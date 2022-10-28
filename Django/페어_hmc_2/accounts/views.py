from urllib.parse import uses_fragment
from django.shortcuts import render, redirect, get_object_or_404

# from .models import User
from django.contrib import messages
from django.contrib.auth import login as my_login, logout as my_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            weight = user.userweights
            tall = user.usertall
            if user.gender == 1:
                fat = (weight * user.userfat) / 100
                standard_w = ((tall / 100) ** 2) * 22
                standard_nf = standard_w * 0.85
                standard_f = standard_w * 0.15
                score = 80 - (standard_nf - (weight - fat)) + (standard_f - fat)
                if score > 150:
                    tier = 1
                elif score > 130:
                    tier = 2
                elif score > 110:
                    tier = 3
                elif score > 90:
                    tier = 4
                elif score > 80:
                    tier = 5
                elif score > 70:
                    tier = 6
                elif score > 60:
                    tier = 7
                else:
                    tier = 8
            else:
                fat = (weight * user.userfat) / 100
                standard_w = ((tall / 100) ** 2) * 22
                standard_nf = standard_w * 0.77
                standard_f = standard_w * 0.23
                score = 80 - (standard_nf - (weight - fat)) + (standard_f - fat)
                if score > 150:
                    tier = 1
                elif score > 130:
                    tier = 2
                elif score > 110:
                    tier = 3
                elif score > 90:
                    tier = 4
                elif score > 80:
                    tier = 5
                elif score > 70:
                    tier = 6
                elif score > 60:
                    tier = 7
                else:
                    tier = 8
            user.tier = tier
            user.score = score
            user.save()
            my_login(request, user)
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


@require_POST
@login_required
def ID_delete(request):
    request.user.delete()
    my_logout(request)
    return redirect("articles:index")


# Create your views here.
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            my_login(request, form.get_user())
            return redirect("articles:index")
    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "accounts/login.html", context)


@login_required
def logout(request):
    my_logout(request)
    messages.warning(request, "로그아웃 하였습니다.")
    return redirect("articles:index")


@login_required
def update(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            weight = user.userweights
            tall = user.usertall
            if user.gender == 1:
                fat = (weight * user.userfat) / 100
                standard_w = ((tall / 100) ** 2) * 22
                standard_nf = standard_w * 0.85
                standard_f = standard_w * 0.15
                score = 80 - (standard_nf - (weight - fat)) + (standard_f - fat)
                if score > 150:
                    tier = 1
                elif score > 130:
                    tier = 2
                elif score > 110:
                    tier = 3
                elif score > 90:
                    tier = 4
                elif score > 80:
                    tier = 5
                elif score > 70:
                    tier = 6
                elif score > 60:
                    tier = 7
                else:
                    tier = 8
            else:
                fat = (weight * user.userfat) / 100
                standard_w = ((tall / 100) ** 2) * 22
                standard_nf = standard_w * 0.77
                standard_f = standard_w * 0.23
                score = 80 - (standard_nf - (weight - fat)) + (standard_f - fat)
                if score > 150:
                    tier = 1
                elif score > 130:
                    tier = 2
                elif score > 110:
                    tier = 3
                elif score > 90:
                    tier = 4
                elif score > 80:
                    tier = 5
                elif score > 70:
                    tier = 6
                elif score > 60:
                    tier = 7
                else:
                    tier = 8
        user.tier = tier
        user.score = score
        user.save()
        return redirect("articles:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


@login_required
def follow(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if request.user == user:
        messages.warning(request, "본인을 팔로우 할 수 없습니다.")
        return redirect("accounts:detail", pk)
    else:
        if request.user in user.followings.all():
            user.followings.remove(request.user)
        else:
            user.followings.add(request.user)
        return redirect("accounts:detail", pk)
