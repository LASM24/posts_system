from django. urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView

posts_patterns = ([
    path('', PostListView.as_view(), name='posts'),
    path("<int:pk>/<slug:slug>/", PostDetailView.as_view(), name="post"),
    path('create/', PostCreateView.as_view(), name='create'),
    path('create/<int:pk>/', PostDeleteView.as_view(), name='delete')
], 'posts')
