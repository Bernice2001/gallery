from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from .models import *
from .forms import *

def main(request):
    gallery = Image.objects.all()
    return render(request, 'images.html' ,{'gallery':gallery})

def search_images(request):
    if 'gallery' in request.GET and request.GET["gallery"]:
        search_term = request.GET.get("gallery")
        searched_gallery = gallery.search_by_gallery(search_term)
        message_brought = {search_term}
        print(searched_gallery)

        return render(request, 'search.html',{"message":message,"image": searched_category})
    else:
        message = "You haven't searched for anything"
    return render(request, 'search.html',{'message':message})

def view_by_location(request, location):
    locations = Image.filter_by_location(location)
    message = location
    return render(request,'location.html',{"image": location, 'message':location}) 

def add_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return False
    
    return render(request, 'form.html', {'form':ImageForm,})          
