from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
	# func views
	# path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
	# generic views
	path('', views.PostListView.as_view(), name='blog-home'),
	path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]