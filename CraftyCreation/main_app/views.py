from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.
def home(request):   
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # Make a 'user' from object with the data from the browser
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # save user to DB
            user = form.save()      
            return redirect('profile')
        else:
            error_message = 'Invalid'
        # if there is  a bad post or get request
    form = UserCreationForm() # creating a blank form  
    context = {'form': form,'error_message': error_message} #this is a dict to send it by the render page
    return render(request, 'registration/signup.html', context)

def profile(request):
    return render(request, 'profile.html')