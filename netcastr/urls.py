from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'netcastr.views.index'),
	url(r'^feeds/$', 'netcastr.views.feedList'),
	url(r'^feeds/create/$', 'netcastr.views.feedCreate'),
	url(r'^feeds/delete/(?P<feed_id>\d+)/$', 'netcastr.views.feedDelete'),
)