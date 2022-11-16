from django.contrib import admin
from django.urls import include, path

from accounts import views
from books.views import BookView, SingleBook
from reviews.views import (
    CreateReview,
    delete_review,
    delete_review_confirmation,
    edit_review,
)
from static_pages.views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="homepage"),
    path("accounts/", include("allauth.urls")),
    path("books/", BookView.as_view(), name="books"),
    path("books/<slug>", SingleBook.as_view(), name="book"),
    path(
        "books/<slug>/create-review",
        CreateReview.as_view(),
        name="create_review",
    ),
    path("reviews/<review_id>", edit_review, name="edit_review"),
    path(
        "reviews/delete_review/<review_id>",
        delete_review_confirmation,
        name="delete_review_confirmation",
    ),
    path(
        "reviews/delete_review/delete/<review_id>",
        delete_review,
        name="delete_review",
    ),
]
