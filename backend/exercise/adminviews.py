from rest_framework import viewsets
from .models import Material, Exercise, ExerciseStep, ExerciseMaterial, ExerciseSport, ExerciseZone, WorkZone
from .serializers import MaterialSerializer, ExerciseSerializer, ExerciseStepSerializer, ExerciseMaterialSerializer, ExerciseSportSerializer, ExerciseZoneSerializer, WorkZoneSerializer
from drf_yasg.utils import swagger_auto_schema

#------------------MATERIAL------------------
# Admin ViewSet
class AdminMaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    @swagger_auto_schema(
        tags=['Admin - Material'],
        operation_description="Custom description for admin material list.",
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Material'],
        operation_description="Custom description for admin material retrieve.",
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Material'],
        operation_description="Custom description for admin material create.",
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Material'],
        operation_description="Custom description for admin material update.",
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Material'],
        operation_description="Custom description for admin material partial update.",
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Material'],
        operation_description="Custom description for admin material delete.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE------------------
# Admin ViewSet
class AdminExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    @swagger_auto_schema(
        tags=['Admin - Exercise'],
        operation_description="Custom description for admin exercise list.",
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise'],
        operation_description="Custom description for admin exercise retrieve.",
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise'],
        operation_description="Custom description for admin exercise create.",
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise'],
        operation_description="Custom description for admin exercise update.",
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise'],
        operation_description="Custom description for admin exercise partial update.",
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise'],
        operation_description="Custom description for admin exercise delete.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_STEPS------------------
# Admin ViewSet
class AdminExerciseStepViewSet(viewsets.ModelViewSet):
    queryset = ExerciseStep.objects.all()
    serializer_class = ExerciseStepSerializer

    @swagger_auto_schema(
        tags=['Admin - Exercise Step'],
        operation_description="Custom description for admin exercise step list.",
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Step'],
        operation_description="Custom description for admin exercise step retrieve.",
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Step'],
        operation_description="Custom description for admin exercise step create.",
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Step'],
        operation_description="Custom description for admin exercise step update.",
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Step'],
        operation_description="Custom description for admin exercise step partial update.",
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Step'],
        operation_description="Custom description for admin exercise step delete.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_MATERIAL------------------
# Admin ViewSet
class AdminExerciseMaterialViewSet(viewsets.ModelViewSet):
    queryset = ExerciseMaterial.objects.all()
    serializer_class = ExerciseMaterialSerializer

    @swagger_auto_schema(
        tags=['Admin - Exercise Material'],
        operation_description="Custom description for admin exercise material list.",
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Material'],
        operation_description="Custom description for admin exercise material retrieve.",
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Material'],
        operation_description="Custom description for admin exercise material create.",
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Material'],
        operation_description="Custom description for admin exercise material update.",
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Material'],
        operation_description="Custom description for admin exercise material partial update.",
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Material'],
        operation_description="Custom description for admin exercise material delete.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_SPORTS------------------
# Admin ViewSet
class AdminExerciseSportViewSet(viewsets.ModelViewSet):
    queryset = ExerciseSport.objects.all()
    serializer_class = ExerciseSportSerializer

    @swagger_auto_schema(
        tags=['Admin - Exercise Sport'],
        operation_description="Custom description for admin exercise sport list.",
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Sport'],
        operation_description="Custom description for admin exercise sport retrieve.",
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Sport'],
        operation_description="Custom description for admin exercise sport create.",
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Sport'],
        operation_description="Custom description for admin exercise sport update.",
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Sport'],
        operation_description="Custom description for admin exercise sport partial update.",
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Sport'],
        operation_description="Custom description for admin exercise sport delete.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_Zone------------------
# Admin ViewSet
class AdminExerciseZoneViewSet(viewsets.ModelViewSet):
    queryset = ExerciseZone.objects.all()
    serializer_class = ExerciseZoneSerializer

    @swagger_auto_schema(
        tags=['Admin - Exercise Zone'],
        operation_description="Custom description for admin exercise zone list.",
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Zone'],
        operation_description="Custom description for admin exercise zone retrieve.",
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Zone'],
        operation_description="Custom description for admin exercise zone create.",
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Zone'],
        operation_description="Custom description for admin exercise zone update.",
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Zone'],
        operation_description="Custom description for admin exercise zone partial update.",
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Exercise Zone'],
        operation_description="Custom description for admin exercise zone delete.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------WORKZONE------------------
# Admin ViewSet
class AdminWorkZoneViewSet(viewsets.ModelViewSet):
    queryset = WorkZone.objects.all()
    serializer_class = WorkZoneSerializer

    @swagger_auto_schema(
        tags=['Admin - Work Zone'],
        operation_description="Custom description for admin work zone list.",
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Work Zone'],
        operation_description="Custom description for admin work zone retrieve.",
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Work Zone'],
        operation_description="Custom description for admin work zone create.",
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Work Zone'],
        operation_description="Custom description for admin work zone update.",
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Work Zone'],
        operation_description="Custom description for admin work zone partial update.",
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Admin - Work Zone'],
        operation_description="Custom description for admin work zone delete.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
