from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from books.models import Book

from .forms import ReviewForm


# Create your views here.
class CreateReview(LoginRequiredMixin, CreateView):
    form_class = ReviewForm
    template_name = "create_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, slug=self.kwargs["slug"])
        context["book"] = book
        return context

    def get_success_url(self):
        from django.urls import reverse

        return reverse("book", kwargs={"slug": self.kwargs["slug"]})

    def form_valid(self, form):
        book = get_object_or_404(Book, slug=self.kwargs["slug"])
        self.object = form.save(commit=False)
        self.object.book = book
        self.object.user_id = self.request.user.pk
        self.object.save
        return super().form_valid(form)
