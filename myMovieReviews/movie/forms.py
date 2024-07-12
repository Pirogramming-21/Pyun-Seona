from django import forms
from .models import Review

class ReviewForm(forms.Form):
    title = forms.CharField(label='Title', max_length=32)
    year_release = forms.IntegerField(label='Year Release')
    genre = forms.CharField(label='Genre', max_length=10)
    scope = forms.FloatField(label='Scope')
    running_time = forms.FloatField(label='Running Time')
    content = forms.CharField(label='Review Content', widget=forms.Textarea)
    director = forms.CharField(label='Director', max_length=10)
    actor = forms.CharField(label='Actor', max_length=10)
    image_url = forms.URLField(label='Image URL', required=False)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'year_release', 'genre', 'scope', 'running_time', 'content', 'director', 'actor']