from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'release_date', 'description', 'poster']

    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if release_date > timezone.now().date():
            raise ValidationError("Release date cannot be in the future")
        return release_date
