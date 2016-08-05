from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	cellphone = models.IntegerField(blank=True, null=True)
	birth = models.DateField(blank=True, null=True)
	profile_img = models.ImageField(upload_to = 'user/%Y/%m/%d', blank=True, null=True)
	back_img = models.ImageField(upload_to = 'user/%Y/%m/%d/back', blank=True, null=True)

	def __str__(self):
		return "Perfil del usuario {}".format(self.user.username)

# Create your models here.