from rest_framework import permissions, viewsets
from .models import Workout
from .serializers import WorkoutSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from users2.permissions import IsUserOrAdmin
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import filters, mixins, status, viewsets, pagination
from rest_framework.exceptions import ValidationError
from datetime import datetime
import re

# Create your views here.
from utils.utils import get_ordered_queryset

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def get_permissions(self):
        permission_classes = [IsUserOrAdmin]
        return [permission() for permission in permission_classes]

    @extend_schema(
        tags=['Workout User'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Workout User'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_workouts_user = self.get_latest()
        serializer = self.serializer_class(latest_workouts_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Workout User'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = WorkoutSerializer(instance)
        return Response(serializer.data)

    @extend_schema(
        tags=['Workout User'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Workout User'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Workout User'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Workout User'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Workout User'],
        responses={200: "OK"}
    )
    # Action pour récupérer le workout selon l'utilisateur et la date
    @action(detail=False, methods=['get'], url_path="by-user-and-date")
    def get_workout_by_user_and_date(self, request):
        user_id = request.query_params.get('user_id')
        date_str = request.query_params.get('date')
        print(request.query_params)
        print(date_str)
        if not user_id or not date_str:
            return Response({"error": "user_id and date parameters are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Removing the non-standard timezone information using regex
            date_str = re.sub(r'\sGMT.*', '', date_str)
            # Parsing the cleaned date string
            date = datetime.strptime(date_str, '%a %b %d %Y %H:%M:%S')
        except ValueError as e:
            return Response({"error": f"Invalid date format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
        workouts = Workout.objects.filter(user_id=user_id, date__date=date.date())
        
        if not workouts.exists():
            return Response([], status=status.HTTP_200_OK)
        
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
