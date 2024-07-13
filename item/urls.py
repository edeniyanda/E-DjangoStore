from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("newitem/", views.newitem, name="new_item"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete", views.delete_item, name="delete_item"),
    path("<int:pk>/edit", views.edititem, name="edit_item"),
]
