from django.urls import path

from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', views.base.post_list, name='post_list'),
    path('teste/', views.base.test, name='teste'),
    path('tag/<slug:tag_slug>/', views.base.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.base.post_detail, name='post_detail'),
    path('<int:post_pk>/share/', views.features.post_share, name='post_share'),
    path('<int:post_pk>/comment/', views.features.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.features.post_search, name='post_search'),
]
