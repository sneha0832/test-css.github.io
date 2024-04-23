from django import forms

from csctest.models import ExhibitRating


class RatingForm(forms.ModelForm):
    class Meta:
        model = ExhibitRating
        fields = ['rating']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 11)])
        }
