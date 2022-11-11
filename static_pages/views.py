from django.shortcuts import render
from django.views.generic import TemplateView

from books.models import Book

# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_books"] = Book.get_latest()
        return context
