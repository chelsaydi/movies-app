from django import forms
from .models import Video
import datetime

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["movie_id", "title", "actor1", "actor2", "director", "genre", "release_year"]
        labels = {
            "movie_id": "MovieID",
            "title": "MovieTitle",
            "actor1": "Actor1Name",
            "actor2": "Actor2Name",
            "director": "DirectorName",
            "genre": "MovieGenre",
            "release_year": "ReleaseYear",
            
        }
        widgets = {
            "release_year": forms.NumberInput(attrs={
                "min": 1888,
                "max": datetime.date.today().year
            }),
        }

    def clean_release_year(self):
        year = self.cleaned_data["release_year"]
        this_year = datetime.date.today().year
        if not (1888 <= year <= this_year):
            raise forms.ValidationError(f"Release year must be between 1888 and {this_year}.")
        return year

