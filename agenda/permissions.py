
from rest_framework.permissions import IsAuthenticated, BasePermission




class UserOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        
        return super().has_object_permission(request, view, obj)