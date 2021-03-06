from xml.dom.minidom import parse
from django.core import serializers
from netcastr.models import Feed, Item
import datetime
import hashlib
import re

def parseFeed(xmlFile, url, user):
	xmldom = parse(xmlFile)
	feedTitle = getText(xmldom.getElementsByTagName('title')[0].childNodes)
	feedDescription = getText(xmldom.getElementsByTagName('description')[0].childNodes)
	feedImageUrl = handleImage(xmldom.getElementsByTagName('image')[0])

	f = Feed(
		curXml = hashlib.sha224(xmldom.toxml()).hexdigest(),
		description = feedDescription,
		imageUrl = feedImageUrl,
		title = feedTitle,
		user = user,
		url = url,
	)

	f.save()

	items = xmldom.getElementsByTagName('item')
	for item in items:
		handleItem(item, f)

	return serializers.serialize("json", Feed.objects.filter(pk=f.id))

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE or node.nodeType == node.CDATA_SECTION_NODE:
            rc.append(node.data)
    return ''.join(rc)

def handleImage(imageNode):
	return getText(imageNode.getElementsByTagName('url')[0].childNodes)

def handleItem(itemNode, feed):
	itemDescription = getText(itemNode.getElementsByTagName('description')[0].childNodes)
	itemMediaType = itemNode.getElementsByTagName('enclosure')[0].getAttribute('type')
	itemMediaUrl = itemNode.getElementsByTagName('enclosure')[0].getAttribute('url')
	dateString = getText(itemNode.getElementsByTagName('pubDate')[0].childNodes)
	itemPubDate = datetime.datetime.strptime(dateString[:25],
		'%a, %d %b %Y %X').strftime('%Y-%m-%d %X')

	itemTitle = getText(itemNode.getElementsByTagName('title')[0].childNodes)

	feed.item_set.create(
		description = itemDescription,
		mediaType = itemMediaType,
		mediaUrl = itemMediaUrl,
		pubDate = itemPubDate,
		title = itemTitle,
	)