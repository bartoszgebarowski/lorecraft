from django.views.generic import DetailView, ListView, TemplateView

from books.models import Book


class BookView(ListView):
    template_name = "books.html"
    model = Book
    paginate_by = 3
    ordering = "-created_at"


class SingleBook(DetailView):
    template_name = "single_book.html"
    model = Book
    pk_url_kwarg = "Book.slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context[
                "is_review_eligible"
            ] = self.request.user.is_review_eligible(
                book_slug=self.kwargs["slug"]
            )
        else:
            context["is_review_eligible"] = False
        context["rating"] = self.model.get_average_rating(
            book_slug=self.kwargs["slug"]
        )
        return context
