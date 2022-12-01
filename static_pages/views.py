from django.shortcuts import render
from django.views.generic import TemplateView

from books.models import Book


class HomeView(TemplateView):
    """Generic index template view"""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """Enrich a context with latest and best rated `Books`"""
        context = super().get_context_data(**kwargs)
        context["latest_books"] = Book.get_latest()
        context["best_books"] = Book.get_best_rated_books()
        return context
