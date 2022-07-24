from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Класс для правки прав пользователя. Является ли он автором или нет.
    """

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
