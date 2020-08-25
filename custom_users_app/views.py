from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from custom_users_app.models import CustomUser
from custom_users_app.forms import AddLoginForm, AddSignupForm

# Create your views here.
def index_view(request):
    return render(request, "homepage.html")

def login_view(request):
    if request.method == "POST":
        form = AddLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data.get("username"),
                password=data.get("password")
            )
            if user:
                login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse("homepage"))
            )

    form = AddLoginForm()
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = AddSignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                displayname=data.get('displayname'),
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))

    form = AddSignupForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))