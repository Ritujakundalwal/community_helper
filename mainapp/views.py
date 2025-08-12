from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import HelpRequest
from django.contrib.auth.decorators import login_required
from django.db.models import Count



# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')

        # create new user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Registered Successfully! Please login.")
        return redirect('login')

    return render(request, 'mainapp/register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')

    return render(request, 'mainapp/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')




def request_help(request):
    if request.method == "POST":
        help_type = request.POST.get('help_type')
        description = request.POST.get('description')
        area = request.POST.get('area')

        new_request = HelpRequest.objects.create(
            seeker=request.user,
            help_type=help_type,
            description=description,
            area=area
        )
        new_request.save()

        messages.success(request, "Your help request has been submitted.")
        return redirect('home')

    return render(request, 'mainapp/request_help.html')


from .models import HelpRequest
from django.contrib.auth.decorators import login_required

@login_required
def view_requests(request):
    # helper user cha area milava pahije, assume we take from profile or input
    # pan ata sarva requests dakhvtoy simple sathi
    requests = HelpRequest.objects.all().order_by('-created_at')

    return render(request, 'mainapp/view_requests.html', {'requests': requests})

from django.shortcuts import get_object_or_404

@login_required
def accept_request(request, pk):
    help_request = get_object_or_404(HelpRequest, pk=pk)

    # Check if already accepted
    if not help_request.is_accepted:
        help_request.is_accepted = True
        help_request.accepted_by = request.user
        help_request.save()
        messages.success(request, "You have accepted the request.")
    else:
        messages.warning(request, "This request is already accepted.")

    return redirect('view_requests')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import HelpRequest

@login_required
def profile(request):
    user = request.user
    
    user_requests = HelpRequest.objects.filter(seeker=user)

    accepted_requests = HelpRequest.objects.filter(accepted_by=user)

    context = {
        'user': user,
        'user_requests': user_requests,
        'accepted_requests': accepted_requests
    }
    return render(request, 'mainapp/profile.html', context)

# mainapp/views.py

from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Count

def top_helpers(request):
    top_helpers = User.objects.annotate(help_count=Count('accepted_helpers')).order_by('-help_count')
    return render(request, 'mainapp/top_helpers.html', {'top_helpers': top_helpers})




