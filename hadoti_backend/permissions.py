from rest_framework import permissions


class IsAdminOrStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin or staff users to edit objects.
    Regular users get read-only access.
    """

    def has_permission(self, request, view):
        # Read permissions for any request (authenticated or not)
        if view.action in ['list', 'retrieve']:
            return True

        # Write permissions only for authenticated admin/staff users
        return request.user.is_authenticated and (
            request.user.is_staff or request.user.is_superuser
        )


class IsAdminOrStaffOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin or staff users.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_staff or request.user.is_superuser
        )