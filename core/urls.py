from django.urls import path, include
from django.contrib.auth import views as auth_view
from .views import index, contact, signup
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", index, name="home_page"),
    path("contact/", contact, name="contact_page"),
    path("signup/", signup, name="signup_page"),
    path("login/", auth_view.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name="login_page"),
]