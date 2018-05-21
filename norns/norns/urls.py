from django.contrib import admin
from django.urls import path, include
from .views import home_view, store_view, about_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('store/', store_view, name='store'),
    path('about/', about_view, name='about'),
    path('api/v1/room/', include('room.urls')),
]
