from rest_framework import permissions


class IsSelf(permissions.BasePermission):
    """
    Object-level permission to only allow creators of an object to edit it.
    """
    message = 'You must be the user.'

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.user == request.user
        return False
