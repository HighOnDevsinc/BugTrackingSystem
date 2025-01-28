
from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('authentication/', include('authentication.urls')),
    path('projects/', include('project.urls')),

]
