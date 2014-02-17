from django.conf.urls.defaults import *
from django.views.static import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asylguiden.views.home', name='home'),
    # url(r'^asylguiden/', include('asylguiden.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    #Include book url
     url(r'^book$', 'book.views.start'),
     url(r'^book/start$', 'book.views.start'),
     url(r'^book/new$', 'book.views.new'),
     url(r'^book/articels$', 'book.views.articels'),
     
     # MEDIA files
      (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
      (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
