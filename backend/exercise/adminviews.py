from rest_framework import viewsets, permissions
from .models import Material, Exercise, ExerciseStep, ExerciseMaterial, ExerciseSport, ExerciseZone, WorkZone
from .serializers import MaterialSerializer, ExerciseSerializer, ExerciseStepSerializer, ExerciseMaterialSerializer, ExerciseSportSerializer, ExerciseZoneSerializer, WorkZoneSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

#------------------MATERIAL------------------
# Admin ViewSet
class AdminMaterialViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Material'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Material'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE------------------
# Admin ViewSet
class AdminExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_STEPS------------------
# Admin ViewSet
class AdminExerciseStepViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = ExerciseStep.objects.all()
    serializer_class = ExerciseStepSerializer

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_MATERIAL------------------
# Admin ViewSet
class AdminExerciseMaterialViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = ExerciseMaterial.objects.all()
    serializer_class = ExerciseMaterialSerializer

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_SPORTS------------------
# Admin ViewSet
class AdminExerciseSportViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = ExerciseSport.objects.all()
    serializer_class = ExerciseSportSerializer

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_Zone------------------
# Admin ViewSet
class AdminExerciseZoneViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = ExerciseZone.objects.all()
    serializer_class = ExerciseZoneSerializer

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------WORKZONE------------------
# Admin ViewSet
class AdminWorkZoneViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = WorkZone.objects.all()
    serializer_class = WorkZoneSerializer

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
