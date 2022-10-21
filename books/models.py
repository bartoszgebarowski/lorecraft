from cloudinary.models import CloudinaryField
from django.db import models


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
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
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

    def __str__(self) -> str:
        return f"{self.title}"

    def get_genre(self):
        return list(self.genre.all())

    get_genre.short_description = "Genre"

    def get_authors(self):
        return list(self.author.all())

    get_authors.short_description = "Authors"


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
