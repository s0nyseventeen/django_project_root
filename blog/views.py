from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# LoginRequiredMixin with classes like decorators:@login_required() with func
from django.contrib.auth.mixins import LoginRequiredMixin

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


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/post_creat.html'
	# success_url = reverse_lazy('blog:blog-home')  # if we don't user get_absolute_url() within model

	def form_valid(self, form):
		# form you're trying to submit, before you do that: take instance -> 
		# set author equal to the current loggined user
		form.instance.author = self.request.user
		# validation of the form
		return super().form_valid(form)





