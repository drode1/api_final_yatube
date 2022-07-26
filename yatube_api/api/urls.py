from django.conf.urls import url
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet, basename='posts')
router_v1.register('v1/groups', GroupViewSet, basename='groups')
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')
router_v1.register('v1/follow', FollowViewSet, basename='follows')

urlpatterns = [
    url('v1/', include('djoser.urls')),
    url('v1/', include('djoser.urls.jwt')),
    path('v1/redoc/', TemplateView.as_view(template_name='redoc.html'),
         name='redoc'
         ),
]
urlpatterns += router_v1.urls
