from reviews.models import Review
from django import forms
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields = ['name','email','stars','review']
        widgets = { 'stars': forms.NumberInput(attrs={'min': 1, 'max': 5})}
    #aboba