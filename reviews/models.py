from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import MyUser
from books.models import Book


class Review(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, editable=False, verbose_name="Updated at"
    )

    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self) -> str:
        return f"{self.book} review"
