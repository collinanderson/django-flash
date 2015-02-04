from django.conf.urls import include, url
from django.views.static import serve

from django.conf import settings

urlpatterns = [
    url(r'', include('app.urls')),

    # django-flash needs to ignore requests to static files, in development mode
    url(r'^media/(?P<path>.*)$', serve, \
          {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]
