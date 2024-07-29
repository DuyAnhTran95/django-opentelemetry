from django.urls import path

from . import views

urlpatterns = [
    path("<int:poll_id>", views.get_by_id, name="poll"),
]