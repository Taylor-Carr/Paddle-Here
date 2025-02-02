from django.urls import path
from .views import HomeView, BlogDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView, AddCommentView, UpdateCommentView, DeleteCommentView, search_view, category_view, post_list
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name="blog_details"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('blog/edit/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('blog/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('total_comment_like/<int:pk>', views.like_comment, name="like_comment"),
    path('blog/comment/edit/<int:pk>', UpdateCommentView.as_view(), name="comment_update"),
    path('blog/comment/delete/<int:pk>/', DeleteCommentView.as_view(), name="delete_comment"),
    path('search/', search_view, name="search"),
    path('category/<str:category_name>/', views.category_view, name='category_detail')
]