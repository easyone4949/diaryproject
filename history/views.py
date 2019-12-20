from django.shortcuts import render
from .models import Album
# Create your views here.
def history(request):
    albums = Album.objects
    return render(request, 'history.html', {'albums':albums})