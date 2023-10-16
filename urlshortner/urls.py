from django.urls import path
from .views import ShortURI , RedirectApiView

urlpatterns = [
    path('api/v1/url/shorten/', ShortURI.as_view(), name='CreateShortURI'),  #post
    path('<str:shorturi>', RedirectApiView.as_view(), name='redirect-view'), #get
    # path('listall/', ShortURI.as_view(), name='getShortURI'), #get
    # path('listall/<int:id>', ShortURI.as_view(), name='getShortURI'),       #get
    path('extend/expiry/', ShortURI.as_view(), name='extendExpiryDate'),  #patch
]
