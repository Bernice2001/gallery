from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.main, name = 'welcome'),
    url('search/', views.search_images, name='searchPage'), 
    url('upload/', views.add_image, name='addPage'), 
    url('location/<location>/', views.view_by_location, name='locationPage'), 


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)