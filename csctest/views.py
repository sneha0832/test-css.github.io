from .models import Exhibit, TypeofPlay, Activity, ExhibitRating
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import PageTimeSpent
import json
from django.http import JsonResponse
import urllib.parse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Exhibit, Child, ExhibitRating
from django.contrib import messages


def html_view(request, pk):
    html_page = get_object_or_404(Exhibit, pk=pk)
    context = {
        'html_page': html_page,
        'exhibit_id': pk,  # Pass the primary key (exhibit ID) to the template
    }
    return render(request, 'exhibit_template.html', context)


def homepage_view(request):
    html_pages = Exhibit.objects.all()  # Retrieve all HTMLPage objects from the database
    return render(request, 'homepage.html', {'html_pages': html_pages})


def Account(request):
    return render(request, "Account.html", {})


def LoginPageView(request):
    return render(request, "login.html", {})


def Resources(request):
    return render(request, "Resources.html", {})


def Play(request):
    return render(request, "Play.html", {})


def custom_logout(request):
    next_page = request.GET.get('next', reverse_lazy('homepage_view'))
    return LogoutView.as_view(next_page=next_page)(request)


@csrf_exempt
@require_http_methods(["POST"])
def get_activities(request):
    try:
        play_type_name = request.POST.get('play_type')
        type_of_play = TypeofPlay.objects.get(TypeName=play_type_name)
        activities = Activity.objects.filter(category=type_of_play).values('activityName', 'description')

        activities_list = [{'activityName': activity['activityName'], 'description': activity['description']} for
                           activity in activities]

        return JsonResponse({
            'typeDescription': type_of_play.description,
            'activities': activities_list
        })

    except TypeofPlay.DoesNotExist:
        return JsonResponse({'error': 'Play type not found'}, status=404)


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


def get_activities_for_exhibit(request, exhibit_name):
    # URL-decode the exhibit_name parameter since it might contain URL-encoded characters
    exhibit_name = urllib.parse.unquote(exhibit_name)

    # Filter activities by the exhibit name
    activities = Activity.objects.filter(ExhibitName=exhibit_name).values(
        'activityName', 'category', 'subcategory', 'description'
    )
    return JsonResponse({'activities': list(activities)})


@login_required
def rate_exhibit(request, exhibit_id):
    exhibit = Exhibit.objects.filter(Exhibit, id=exhibit_id)
    children = Child.objects.filter(parent=request.user)  # Ensure 'parent' is used here

    if request.method == 'POST':
        child_id = request.POST.get('child_id')
        rating = request.POST.get('rating')

        # Use 'parent' as the field name as defined in your Child model
        child = get_object_or_404(Child, id=child_id, parent=request.user)

        # Use 'rating' after ensuring it can be cast to an integer safely
        ExhibitRating.objects.update_or_create(
            child=child,
            exhibit=exhibit,
            defaults={'rating': int(rating)}
        )
        return redirect('some_success_url_name')  # Replace with your actual success URL name

    return render(request, 'exhibit_template.html', {
        'html_page': exhibit,
        'children': children,
        'ratings_range': range(1, 11)
    })
