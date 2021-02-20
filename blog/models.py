from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


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

	# django need to know how to find the location to the specific Post
	# we don't need to provide success_url() in CreateView
	#     if we define get_absolute_url
	def get_absolute_url(self):
		'''reverse() - return full URL to that route as a str,
		redirect() - just redirect you to the specific route
		'''
		return reverse('blog:post-detail', kwargs={'pk': self.pk})


