from django import forms
class ReviewForm(forms.Form):
    name=forms.CharField(max_length=15)
    email=forms.EmailField()
    review = forms.CharField(widget=forms.Textarea)
    #aboba