from django.urls import path
from .views import ShortURI

urlpatterns = [
    path('create/shorturi/', ShortURI.as_view(), name='Create Short URI'),  #post
    path('listall/', ShortURI.as_view(), name='get Short URI'),
    path('listall/<int:id>', ShortURI.as_view(), name='get Short URI'),       #get
    path('update/uri/', ShortURI.as_view(), name='update short uri'),    #put
    path('extend/expiry/', ShortURI.as_view(), name='extend expiry date'),  #patch
    path('delete/uri/', ShortURI.as_view(), name='delete uri'),      #delete
]
