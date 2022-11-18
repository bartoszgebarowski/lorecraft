from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    def is_review_eligible(self, book_slug):
        from reviews.models import Review

        exists = Review.objects.filter(
            user_id=self.pk, book__slug=book_slug
        ).exists()

        return not exists
