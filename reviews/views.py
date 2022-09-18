from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from . import forms
from books import models as book_models
from movies import models as movie_models


def create_book_review(request, pk):

    if request.user.is_authenticated is False:
        messages.info(request, "Please log in.")
        return redirect(reverse("users:login"))

    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        try:
            book = book_models.Book.objects.get(pk=pk)
            if form.is_valid():
                review = form.save()
                review.created_by = request.user
                review.book = book
                review.save()
                messages.success(request, "Created Book Review")
            else:
                messages.error(request, "Invalid Data")
            return redirect(reverse("books:book", kwargs={"pk": pk}))

        except book_models.Book.DoesNotExist:
            return redirect(reverse("core:home"))


def create_movie_review(request, pk):

    if request.user.is_authenticated is False:
        return redirect(request.META.get("HTTP_REFERER"))

    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        try:
            movie = movie_models.Movie.objects.get(pk=pk)
            if form.is_valid():
                review = form.save()
                review.created_by = request.user
                review.movie = movie
                review.save()
                messages.success(request, "Created Movie Review")
            else:
                messages.error(request, "Invalid Data")
            return redirect(reverse("movies:movie", kwargs={"pk": pk}))

        except movie_models.Movie.DoesNotExist:
            return redirect(reverse("core:home"))
