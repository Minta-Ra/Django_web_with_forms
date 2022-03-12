from django import forms

from .models import Album, Artist


class AlbumForm(forms.ModelForm):

    artist = forms.ModelChoiceField(Artist.objects.all())

    class Meta:
        model = Album
        fields = ('title', 'year', 'stock_level', 'artist')