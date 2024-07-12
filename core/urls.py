from django.urls import path, include
from .views import index, contact, signup


app_name = "core"

urlpatterns = [
    path("", index, name="home_page"),
    path("contact/", contact, name="contact_page"),
    path("signup/", signup, name="signup_page"),
]