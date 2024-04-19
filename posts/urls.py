from django. urls import path
from .views import PostListView

posts_patterns = ([
    path('', PostListView.as_view(), name='posts')
], 'posts')
