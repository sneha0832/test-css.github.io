from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from csctest import views
from django.contrib import admin
from django.urls import re_path
from .views import rate_exhibit

from csctest.views import homepage_view, record_time_spent, html_view, custom_logout

urlpatterns = [
                  path('', homepage_view, name='homepage_view'),
                  path('record_time_spent/', record_time_spent, name='record_time_spent'),
                  path('exhibit/<int:pk>/', html_view, name='html_view'),
                  path('Account.html/', views.Account, name='Account'),
                  path("login.html", views.LoginPageView, name='login'),
                  path('get_activities/', views.get_activities, name='get_activities'),
                  path("Resources.html", views.Resources, name='Resources'),
                  path("Play.html", views.Play, name='Play'),
                  path('admin/', admin.site.urls),
                  path('logout/', custom_logout, name='custom_logout'),
                  path('get-activities-for-exhibit/<str:exhibit_name>/', views.get_activities_for_exhibit, name='get_activities_for_exhibit'),
                  path('exhibit/rate/<int:exhibit_id>/', rate_exhibit, name='rate_exhibit')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
