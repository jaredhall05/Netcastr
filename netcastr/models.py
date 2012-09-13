from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
	curXml = models.TextField()
	description = models.TextField()
	imageUrl = models.URLField()
	title = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	url = models.URLField()

	def __unicode__(self):
		return self.title

class Item(models.Model):
	description = models.TextField()
	feed = models.ForeignKey(Feed)
	mediaType = models.CharField(max_length=200)
	mediaUrl = models.URLField()
	pubDate = models.DateTimeField('date published')
	title = models.CharField(max_length=200)
	viewed = models.BooleanField()

	def __unicode__(self):
		return self.title