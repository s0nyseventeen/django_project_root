from django.urls import path

from .views import(
	# home,
	about,
	PostListView,
	UserPostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
)

app_name = 'blog'

urlpatterns = [
	# func views
	# path('', home, name='blog-home'),
	path('about/', about, name='blog-about'),
	# generic views
	path('', PostListView.as_view(), name='blog-home'),
	path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/create/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]