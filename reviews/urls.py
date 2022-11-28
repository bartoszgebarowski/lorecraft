from django.urls import path

from reviews.views import (
    delete_review,
    delete_review_confirmation,
    edit_review,
)

urlpatterns = [
    path("<review_id>", edit_review, name="edit_review"),
    path(
        "delete-review/<review_id>",
        delete_review_confirmation,
        name="delete_review_confirmation",
    ),
    path(
        "delete-review/delete/<review_id>",
        delete_review,
        name="delete_review",
    ),
]
