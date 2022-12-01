from django.urls import path

from static_pages.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
]
