from rest_framework import relations, serializers, validators

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор для групп.
    """

    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для постов.
    """
    author = relations.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для комментариев пользователей.
    """
    author = relations.SlugRelatedField(slug_field='username', read_only=True)
    post = relations.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор для подписок.
    """
    user = relations.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )

    following = relations.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    def validate_following(self, following):
        """
        Проверяем того, что пользователь не подписывается сам на себя.
        """
        if self.context.get('request').user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя')
        return following

    class Meta:
        fields = ('user', 'following',)
        model = Follow

        validators = [
            # Проверяем, что в базе нет дубликатов.
            validators.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
            ),
        ]
