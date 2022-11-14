from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content", "rating"]
