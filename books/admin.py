from django.contrib import admin

# Register your models here.
from .models import Author, Book, ExamplePage, Genre


class BookAdmin(admin.ModelAdmin):
    list_filter = ["author", "title", "genre"]
    list_display = (
        "title",
        "is_visible",
        "is_featured",
        "get_authors",
        "get_genre",
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(ExamplePage)
