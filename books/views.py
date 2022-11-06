from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from books.models import Book

# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_books"] = Book.get_latest()
        return context


class BookView(ListView):
    template_name = "books.html"
    model = Book
    paginate_by = 3
    ordering = "-created_at"
