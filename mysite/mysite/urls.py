from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
