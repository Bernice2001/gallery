from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import image
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Gallery shop')

def main(request):
    context={
     'galleries' gallery.objects.all()
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

    def view_by_location(request, location):
      locations = Image.filter_by_location(location)
      message = location
        return render(request,'location.html',{"image": location, 'message':location})       