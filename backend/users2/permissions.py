from rest_framework import permissions
from rest_framework.request import Request
from .models import User


class UserViewSetPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        # If trying to create a User, OK
        if request.method == "POST":
            return True
        
        # Else, needs to be authenticated
        if request.user.is_authenticated:
            return True
        
        return False
        

    def has_object_permission(self, request: Request, view, obj: User):
        # PATCH, PUT, DELETE => Only same person or admin or staff
        # GET: Anyone
        if request.method == "GET":
            return True
        
        user_is_same = obj.id == request.user.id
        user_is_admin_or_staff = request.user.is_superuser or request.user.is_coach
        
        return user_is_same or user_is_admin_or_staff
        