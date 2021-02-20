from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# LoginRequiredMixin with classes like decorators:@login_required() with func
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

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
	paginate_by = 10


class UserPostListView(generic.ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 10

	# override model queryset(what we want to display)
	def get_queryset(self):
		# get a username from url if user exists
		user = get_object_or_404(User, username=self.kwargs.get('username'))  
		return Post.objects.filter(author=user).order_by('-data_posted')


class PostDetailView(generic.DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post_detail'


# LoginRequiredMixin, UserPassesTestMixin must be to left in the inheritance
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/post_creat.html'
	# if we don't user get_absolute_url() within model
	# success_url = reverse_lazy('blog:blog-home')  

	def form_valid(self, form):
		# form you're trying to submit, before you do that: take instance -> 
		# set author equal to the current loggined user
		form.instance.author = self.request.user
		# validation of the form
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/post_update.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	# test_func our user passes test to see if our user passes a certain test
	    # condition
	def test_func(self):
		'''getting exact post that we're currently updating'''
		post = self.get_object()  # getting get_object() from UpdateView
		# the same as: True if self.request.user == post.author else False
		if self.request.user == post.author:  # check the post's author
			return True
		else:
			return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:  # check the post's author
			return True
		else:
			return False





