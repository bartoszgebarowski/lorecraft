from django.urls import path

from books.views import BookView, SingleBook

urlpatterns = [
    path("books/", BookView.as_view(), name="books"),
    path("books/<slug>", SingleBook.as_view(), name="book"),
]
