from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostSearch, PostUpdate, PostDelete, ArticleCreate, ArticleUpdate, ArticleDelete

urlpatterns = [
  path('', PostList.as_view(), name='post_list'),
  path('<int:pk>', PostDetail.as_view(), name='post_detail'),
  path('news/search/', PostSearch.as_view(), name='post_search'),
  path('news/create', PostCreate.as_view(), name='post_create'),
  path('articles/create/', ArticleCreate.as_view(), name='article_create'),
  path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
  path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
  path('articles/<int:pk>/update/', ArticleUpdate.as_view(), name='post_update'),
  path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='post_delete'),
    ]