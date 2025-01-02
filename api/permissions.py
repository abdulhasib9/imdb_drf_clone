from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
        #admin_permission = bool(request.user and request.user.is_staff)
        #return request.method == 'GET' or admin_permission
        
        
class AuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #return super().has_object_permission(request, view, obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.author == request.user