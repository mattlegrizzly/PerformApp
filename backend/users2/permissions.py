from rest_framework import permissions
from rest_framework.request import Request
from .models import User


class UserViewSetPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        print(request)
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

from rest_framework.exceptions import PermissionDenied

class IsUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Si la méthode est une opération de lecture (GET)
        if request.method in permissions.SAFE_METHODS:
            # Si l'utilisateur est administrateur, autorisez l'accès
            if request.user.id and request.user.is_superuser:
                return True
            # Si l'utilisateur est authentifié mais pas administrateur, autorisez l'accès uniquement à ses propres infos
            elif request.user.id and not request.user.is_superuser:
                return True
            # Sinon, refusez l'accès
            else:
                return False

        # Si la méthode est une opération de modification (POST, PUT, PATCH, DELETE),
        # vérifie si l'utilisateur est le même que celui fourni dans les données
        user_id = request.data.get('user')
        if user_id and int(user_id) == request.user or request.user.is_superuser :
            return True

        # Si l'utilisateur n'est ni admin ni le même que celui fourni dans les données, refusez l'accès
        return False

    def has_object_permission(self, request, view, obj):
        # Si l'utilisateur est administrateur, autorisez l'accès
        if request.user and request.user.is_superuser:
            return True

        # Si l'utilisateur n'est pas authentifié, refusez l'accès
        if not request.user.is_authenticated:
            return False

        # Vérifie si l'utilisateur est le même que celui associé à l'objet
        return obj.user == request.user
    
    
    def has_object_list_permission(self, request, view):
        # Si la méthode est une opération de lecture (GET) et l'utilisateur n'est pas admin
        if request.method in permissions.SAFE_METHODS and request.user and not request.user.is_superuser:
            # Filtrer les objets pour n'afficher que ceux associés à l'utilisateur connecté
            view.queryset = view.queryset.filter(user=request.user)
        # Autoriser l'accès pour les méthodes de lecture (GET) ou pour les administrateurs
        return True