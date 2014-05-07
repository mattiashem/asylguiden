#from django.conf.urls.defaults import *
from django.views.static import *
from django.conf import settings
from django.conf.urls import patterns, url, include
from filebrowser.sites import site
from django.contrib import admin
admin.autodiscover()

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

     url(r'^about$', 'book.views.about'),
     url(r'^support$', 'book.views.support'),
     url(r'^supporters$', 'book.views.supporters'),
     url(r'^help$', 'book.views.help'),
     url(r'^tech$', 'book.views.tech'),
     url(r'^book$', 'book.views.start'),
     url(r'^book/start$', 'book.views.start'),
     url(r'^book/new$', 'book.views.new'),
     url(r'^book/question$', 'book.views.question'),
     url(r'^book/new-question$', 'book.views.writeqestion'),
     url(r'^book/search-question$', 'book.views.searchquestion'),
     url(r'^book/articels$', 'book.views.articels'),
     url(r'^book/articel/$', 'book.views.articels'),
     url(r'^book/articel/(\w+)/$', 'book.views.view_articel'),
     url(r'^book/tags/(\w+)/$', 'book.views.view_tags'),
     url(r'^book/location/(\w+)/$', 'book.views.view_location'),
     url(r'^book/delete/(\w+)/$', 'book.views.view_delete'),
     url(r'^book/change/(\w+)/$', 'book.views.view_change'),
     url(r'^book/tags$', 'book.views.top_ten_tags'),
     url(r'^book/location$', 'book.views.top_ten_location'),
     url(r'^book/search$', 'book.views.search_articels'),
     url(r'^book/(\w+)/(\w+)/$', 'book.views.view_location_tags'),
     url(r'^users/register$', 'users.views.register'),
     url(r'^users/login$', 'users.views.login'),
     url(r'^users/logout$', 'users.views.logout'),
     url(r'^users/mypage$', 'users.views.mypage'),
     url(r'^users/resetpassword/(\w+)/$', 'users.views.resetpassword'),
     url(r'^users/lostpassword$', 'users.views.lostpassword'),
     url(r'^i18n/', include('django.conf.urls.i18n')),

     #MEdia upload
     url(r'book/myupload$', 'book.views.upload_file', name = 'myupload' ),
     url(r'book/media$', 'book.views.media', name = 'myupload' ),
     url(r'^$', 'book.views.start'),

     # MEDIA files
     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
     (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)
