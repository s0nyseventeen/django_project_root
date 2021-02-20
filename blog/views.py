from django.shortcuts import render
from django.views import generic

from .models import Post


# func views
# def home(request):
# 	posts = Post.objects.all()
# 	context = {'posts': posts}
# 	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html')


# generic views
class PostListView(generic.ListView):
	model = Post
	template_name = 'blog/home.html'  # default: <app>/<model>_<viewtype>.html
	context_object_name = 'posts'  # default: <object_list>
	ordering = ['-data_posted']


class PostDetailView(generic.DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post_detail'

