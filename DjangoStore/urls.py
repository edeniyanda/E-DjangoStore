
from django.contrib import admin
from django.urls import path
from core.views import (index, contact)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home_page"),
    path('contact/', contact, name="contact_page"),
]
