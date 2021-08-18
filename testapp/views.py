from django.shortcuts import render
from .models import Album
# Create your views here.
def home(request):
    albums = Album.objects.all()
    context ={
    'albums':albums
    }
    return render(request, 'test/index.html',context)