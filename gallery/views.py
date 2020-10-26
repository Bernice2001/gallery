from django.shortcuts import render
from django.http  import HttpResponse
from .models import image
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Gallery shop')

def main(request):
    context={
        'galleries'Gallery.objects.all()
    }
    return render(request, 'galleries/index.html' ,context)

def search_gallery(request):
    if 'gallery' in request.GET and request.GET["gallery"]:
        search_term = request.GET.get("gallery")
        searched_gallery = gallery.search_by_gallery(search_term)
        message brought = {search_term}
        print(searched_gallery)

                return render(request, 'search.html',{"message":message,"image": searched_category})
       else:
        message = "You haven't searched for anything"
        return render(request, 'search.html',{'message':message})
        
