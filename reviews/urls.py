from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("<int:pk>/createbook", views.create_book_review, name="createbook"),
    path("<int:pk>/createmovie", views.create_book_review, name="createmovie"),
]
