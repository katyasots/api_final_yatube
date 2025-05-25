from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')

comment_router = routers.DefaultRouter()
comment_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/', include(comment_router.urls))
]
