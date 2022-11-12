from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from books.models import Book
from reviews.forms import ReviewForm
from reviews.models import Review


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


class SingleBook(DetailView):
    template_name = "single_book.html"
    model = Book
    pk_url_kwarg = "Book.slug"


def create_review(request, slug):
    if request.method == "post":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse("book", kwargs={"id": form.cleaned_data["book_id"]})
            )
    form = ReviewForm()
    context = {"form": form}
    return render(request, "create_review.html", context)
