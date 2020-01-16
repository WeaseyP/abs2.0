from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('population/', include('population.urls')),
    path('admin/', admin.site.urls),
]