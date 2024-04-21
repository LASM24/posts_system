from django. urls import path
from .views import PostListView, PostDetailView, PostCreateView

posts_patterns = ([
    path('', PostListView.as_view(), name='posts'),
    path("<int:pk>/<slug:slug>/", PostDetailView.as_view(), name="post"),
    path('create/', PostCreateView.as_view(), name='create')
], 'posts')
