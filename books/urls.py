from django.urls import path

from books.views import BookView, SingleBook
from reviews.views import CreateReview

urlpatterns = [
    path("", BookView.as_view(), name="books"),
    path("<slug>", SingleBook.as_view(), name="book"),
    path(
        "<slug>/create-review",
        CreateReview.as_view(),
        name="create_review",
    ),
]
