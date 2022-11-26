from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models import Avg


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, editable=False, verbose_name="Updated at"
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, editable=False, verbose_name="Updated at"
    )

    def __str__(self) -> str:
        return f"{self.genre}"


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    is_featured = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)
    year_of_published = models.IntegerField()
    description = models.TextField()
    title_image = CloudinaryField("image", default="placeholder")
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, editable=False, verbose_name="Updated at"
    )

    @property
    def is_img_default(self):
        url = self.title_image.url
        url_split = str(url).split("/")
        if url_split and url_split[-1] == "placeholder":
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{self.title}"

    def get_genre(self):
        return list(self.genres.all())

    def get_authors(self):
        return list(self.authors.all())

    @classmethod
    def get_latest(cls, limit=3):
        latest_books = (
            cls.objects.filter(is_visible=True)
            .order_by("-created_at")
            .all()[:limit]
        )
        return latest_books

    @classmethod
    def get_average_rating(cls, book_slug):
        rating = (
            cls.objects.filter(reviews__is_approved=True, slug=book_slug)
            .all()
            .aggregate(Avg("reviews__rating"))
        )
        return rating["reviews__rating__avg"]

    @classmethod
    def get_best_rated_books(cls, limit=3):
        best_books = (
            cls.objects.filter(reviews__is_approved=True)
            .annotate(average_rating=Avg("reviews__rating"))
            .order_by("-average_rating")[:limit]
            .all()
        )
        return best_books

    get_authors.short_description = "Authors"
    get_genre.short_description = "Genre"


class ExamplePage(models.Model):
    example_page = CloudinaryField("image", default="placeholder")
    books = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="example_pages"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, editable=False, verbose_name="Updated at"
    )

    def __str__(self) -> str:
        return f"{self.books}"
