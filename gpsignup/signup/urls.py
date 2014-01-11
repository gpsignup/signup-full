from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from signup import views

'''
urlpatterns = patterns('',
    url(r'^$', 'signup.views.index'),
    url(r'^create/$', 'signup.views.create'),
    url(r'^results/(?P<event_id>\d+)/$', 'signup.views.results'),
    url(r'^view/(?P<event_id>\d+)/$', 'signup.views.view'),
    url(r'^manage/$', 'signup.views.manage'),
    url(r'^signup/$', 'signup.views.signup'),
    url(r'^thanks/$', 'signup.views.thanks'),
)
'''

# For testing Django REST Framework only: 
urlpatterns = patterns('signup.views',
	url(r'^locations/$', views.LocationList.as_view()),
    url(r'^location/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),
    url(r'^accesskeys/$', views.AccessKeyList.as_view()),
    url(r'^accesskey/(?P<pk>[0-9]+)/$', views.AccessKeyDetail.as_view()),
    url(r'^events/$', views.EventList.as_view()),
    url(r'^event/(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
    url(r'^people/$', views.PersonList.as_view()),
    url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view()),
    url(r'^slots/$', views.SlotList.as_view()),
    url(r'^slot/(?P<pk>[0-9]+)/$', views.SlotDetail.as_view()),    
)

urlpatterns = format_suffix_patterns(urlpatterns)
