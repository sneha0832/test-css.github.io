from django.contrib.auth import login
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ChildForm
from .models import ChatbotResponse, Child
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# from .models import PageTimeSpent
import json


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Path to your login template
    redirect_authenticated_user = True  # Redirect users who are already logged in
    next_page = reverse_lazy('homepage_view')  # Redirect to homepage upon successful login

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user
            send_mail(
                'Welcome to our site!',
                f'Hi {user.username}, thank you for registering with our site.',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            print("Redirecting to home.")  # Debug print
            return redirect('homepage_view')
        else:
            print("Form is not valid:", form.errors)  # Print form errors for debugging
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})


# views.py in your app


def custom_logout(request):
    next_page = request.GET.get('next', reverse_lazy('homepage_view'))
    return LogoutView.as_view(next_page=next_page)(request)


def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.parent = request.user
            child.save()
            return redirect('Account')  # Redirect to the account page
    else:
        form = ChildForm()
    children = request.user.children.all()
    return render(request, 'Account.html', {'form': form, 'children': children})


# Assuming this is in the 'accounts' app


@login_required
def account_view(request):
    children = request.user.children.all()
    return render(request, 'Account.html', {'children': children})


# views.py in your Django app


def chatbot_api(request):
    user_input = request.GET.get('input', '')
    if "activity ideas" in user_input:
        activities = generate_activity_ideas(request.user)
        return JsonResponse({'message': " ".join(activities)})
    try:
        response = ChatbotResponse.objects.get(trigger__icontains=user_input)
        return JsonResponse({'message': response.response})
    except ChatbotResponse.DoesNotExist:
        return JsonResponse({'message': "Sorry, I didn't understand that."})


def generate_activity_ideas(user):
    children = Child.objects.filter(parent=user)
    ideas = []
    for child in children:
        if child.age < 5:
            ideas.append("Consider simple puzzles or outdoor play in safe environments.")
        elif child.age < 10:
            ideas.append("Team sports, reading clubs, or science kits could be exciting.")
        else:
            ideas.append("Advanced model building, coding camps, or sports leagues are great.")
    return ideas


# this view handles the incoming data about time spent
@require_POST
@login_required
def record_time_spent(request):
    data = json.loads(request.body)
    PageTimeSpent.objects.create(
        user=request.user,
        url=data['url'],
        time_spent=data['time_spent']
    )
    return JsonResponse({"status": "success"})
