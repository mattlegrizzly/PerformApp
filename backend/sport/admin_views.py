from rest_framework import permissions, viewsets
from .models import Sport, SportsUser
from .serializers import SportSerializer, SportsUserSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

#------------------SPORT------------------
# Admin ViewSet
class AdminSportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def get_queryset(self):
        queryset = Sport.objects.all()
        return queryset

    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = Sport.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        if request.query_params.get("itemsPerPage"):
            self.pagination_class.page_size = request.query_params.get("itemsPerPage")
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sport'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sport'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------SPORT_USER------------------
# Admin ViewSet
class AdminSportsUserViewSet(viewsets.ModelViewSet):
    queryset = SportsUser.objects.all()
    serializer_class = SportsUserSerializer
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)