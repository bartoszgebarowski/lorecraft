from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("static_pages.urls")),
    path("accounts/", include("allauth.urls")),
    path("books/", include("books.urls")),
    path("reviews/", include("reviews.urls")),
]
