from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import CreateView

from books.models import Book
from reviews.models import Review

from .forms import ReviewForm


class CreateReview(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Generic `Review` create view"""

    form_class = ReviewForm
    template_name = "create_review.html"

    def get_context_data(self, **kwargs):
        """Enrich context with additional `Book` data"""
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, slug=self.kwargs["slug"])
        context["book"] = book
        return context

    def test_func(self):
        """Checks if `User` has permission to create `Review` and returns
        True else False"""
        if self.request.user.is_authenticated:
            return self.request.user.is_review_eligible(
                book_slug=self.kwargs["slug"]
            )
        else:
            return False

    def get_success_url(self):
        """Return success `Book` url"""
        from django.urls import reverse

        return reverse("book", kwargs={"slug": self.kwargs["slug"]})

    def form_valid(self, form):
        """Validated form save with success message"""
        book = get_object_or_404(Book, slug=self.kwargs["slug"])
        self.object = form.save(commit=False)
        self.object.book = book
        self.object.user_id = self.request.user.pk
        self.object.save()

        messages.success(
            self.request, f"Review successfully added to {book.title}"
        )

        return super().form_valid(form)


def edit_review(request, review_id):
    """View that validates and renders edit `Review` form"""
    review = get_object_or_404(Review, id=review_id)
    context = {}

    if review.user != request.user:
        raise PermissionDenied
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review.is_approved = False
            form.save()
            messages.success(request, message="Review succesfully edited")
            return redirect(reverse("book", kwargs={"slug": review.book.slug}))
        else:
            context["form"] = form
    else:
        context["form"] = ReviewForm(instance=review)
    context["instance"] = review
    return render(request, "edit_review.html", context)


def delete_review(request, review_id):
    """View that remove user `Review` from `Book`"""
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        raise PermissionDenied
    else:
        review.delete()
        messages.success(request, message="Review succesfully deleted")
        return redirect(reverse("book", kwargs={"slug": review.book.slug}))


def delete_review_confirmation(request, review_id):
    """View that renders `Review` delete_confirmation template"""
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        raise PermissionDenied
    else:
        context = {
            "instance": review,
        }
        return render(request, "delete_review_confirmation.html", context)
