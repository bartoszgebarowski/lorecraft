from django.urls import path

from reviews.views import (
    CreateReview,
    delete_review,
    delete_review_confirmation,
    edit_review,
)

urlpatterns = [
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
