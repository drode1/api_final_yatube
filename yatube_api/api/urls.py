from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register(r'v1/posts', PostViewSet, basename='posts')
router_v1.register(r'v1/groups', GroupViewSet, basename='groups')
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')
router_v1.register(r'v1/follow', FollowViewSet, basename='follows')

urlpatterns = [
    url(r'v1/', include('djoser.urls')),
    url(r'v1/', include('djoser.urls.jwt')),

]
urlpatterns += router_v1.urls
