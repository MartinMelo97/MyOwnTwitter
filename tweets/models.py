from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Tweet(models.Model):
	user = models.ForeignKey(User, related_name="tuits")
	username = models.CharField(max_length=50)
	content = models.CharField(max_length=140)
	date = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ("-date",)

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse('tweets:details', args=[self.id])

# Create your models here.
