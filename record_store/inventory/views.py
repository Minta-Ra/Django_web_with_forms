from django.shortcuts import redirect, render
from django.http import HttpResponse
from inventory.models import *
from .forms import AlbumForm

def index(request):
    artists = Artist.objects.all()
    return render(request, "inventory/index.html", locals())

# Conditional logic if comes GET or POST request
def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('index')
    else:
        form = AlbumForm()
        # passed in request object, template ---{'form':form} Key:value
        return render(request, "inventory/album_form.html", {'form':form})

