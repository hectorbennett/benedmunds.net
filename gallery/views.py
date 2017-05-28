from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Artwork

def artwork(request):
	Artworks = Artwork.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
	return render(request, 'artwork.html', {'Artworks': Artworks})

def artwork_detail(request, pk):
	Work = Artwork.objects.get(pk=pk)
	return render(request, 'artwork_detail.html', {'Work': Work})
