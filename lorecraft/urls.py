from allauth.account import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("static_pages.urls")),
    path("signup/", views.signup, name="account_signup"),
    path("login/", views.login, name="account_login"),
    path("logout/", views.logout, name="account_logout"),
    path("books", include("books.urls")),
    path("reviews", include("reviews.urls")),
]
