from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    message = "Изменение чужого контента запрещено!"

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user or \
                request.method in \
                permissions.SAFE_METHODS:
            return True
        else:
            return False
