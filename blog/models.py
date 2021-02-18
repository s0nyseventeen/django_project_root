from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	# auto_now=True: we would update the date posted to the current datetime
		# every time the post was updated
	# auto_now_add=True: would set date posted to the current date time only
		# when this object is created 
	data_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title