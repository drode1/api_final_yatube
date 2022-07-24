from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, pagination, filters

from posts.models import Post, Group, Follow
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, \
    FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Вью сет для работы с постами.
    """
    serializer_class = PostSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        if self.action == 'detail':
            return get_object_or_404(Post, pk=self.kwargs['pk'])
        return Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вью сет для работы с группами.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Вью сет для работы с комментариями пользователей.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.get_post().comments


class FollowViewSet(viewsets.ModelViewSet):
    """
    Вью сет для работы с подписками пользователей.
    """
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
