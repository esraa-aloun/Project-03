from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def home(request):   
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



def profile(request):
    return render(request, 'profile.html')

def saveProfile(request):
    pass
    # if request.method == 'POST':


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid form entries")
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "registration/signup.html", context)

