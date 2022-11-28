from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        """Model `Review` form to Create and edit with radio buttons as
        selection for rating
        """

        model = Review
        fields = ["content", "rating"]
        labels = {"content": ("Review content"), "rating": ("Review rating")}

    rating = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=[(f"{i}", f"{i}") for i in range(1, 11)],
    )
