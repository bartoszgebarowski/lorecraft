from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content", "rating"]
        labels = {"content": ("Review content"), "rating": ("Review rating")}

    rating = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={"class": "d-flex gap-5px form-control"}
        ),
        choices=[(f"{i}", f"{i}") for i in range(1, 11)],
    )
