from django.contrib import admin

# Register your models here.
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """View Review in admin panel"""

    list_filter = ["user", "book", "is_approved"]
    list_display = (
        "book",
        "user",
        "is_approved",
    )


admin.site.register(Review, ReviewAdmin)
