from urllib2 import urlopen, URLError, HTTPError
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import feedParser
from models import Feed

@login_required
def index(request):
	return render_to_response('netcastr/index.html', context_instance = RequestContext(request))

@login_required
def feedList(request):
	return HttpResponse(serializers.serialize("json", Feed.objects.filter(user=request.user.id)), mimetype='application/json')
	

@login_required
def feedCreate(request):

	feedurl = request.POST['feedUrl']
	#feedurl = 'http://feeds.twit.tv/tnt_video_large'
	try:
	    response = urlopen(feedurl)
	except HTTPError, e:
	    return HttpResponse('The server couldn\'t fulfill the request.<br />Error code: ', e.code)
	except URLError, e:
	    return HttpResponse('We failed to reach a server.<br />Reason: ', e.reason)
	else:
		return HttpResponse(feedParser.parseFeed(response, feedurl, request.user), mimetype='application/json')

#@login_required
#def feedDelete(request, feed_id):
