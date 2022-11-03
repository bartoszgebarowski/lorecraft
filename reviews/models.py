from django.db import models

from accounts.models import MyUser
from books.models import Book

# Create your models here.


class Review(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    context = models.TextField()
    rating = models.IntegerField(default=1)
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
