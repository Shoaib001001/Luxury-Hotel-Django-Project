from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('recipes/', include('recipes.urls')),
    path('auth/', include('authentication.urls')),
    path('contact/', include('contact.urls')),
]