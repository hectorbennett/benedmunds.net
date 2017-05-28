from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def artwork(request):
	return render(request, 'artwork.html')

def info(request):
	return render(request, 'info.html')
