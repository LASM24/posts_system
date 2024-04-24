from django. urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

posts_patterns = ([
    path('', PostListView.as_view(), name='posts'),
    path("<int:pk>/<slug:slug>/", PostDetailView.as_view(), name="post"),
    path('create/', PostCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('updated/<int:pk>/', PostUpdateView.as_view(), name='update')
], 'posts')
