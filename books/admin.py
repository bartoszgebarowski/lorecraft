from django.contrib import admin

from .models import Author, Book, ExamplePage, Genre


class BookAdmin(admin.ModelAdmin):
    """View Book in admin panel"""

    list_filter = ["authors", "title", "genres"]
    list_display = (
        "title",
        "is_visible",
        "is_featured",
        "get_authors",
        "get_genre",
    )
    prepopulated_fields = {
        "slug": ("title",),
    }


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(ExamplePage)
