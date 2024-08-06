from rest_framework import permissions, viewsets
from .models import Workout
from .serializers import WorkoutSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from users2.permissions import IsUserOrAdmin
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import filters, mixins, status, viewsets, pagination
from rest_framework.exceptions import ValidationError
from django.utils.timezone import make_aware
from django.db.models import Count
from datetime import datetime, timedelta
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
    
    @extend_schema(
        tags=['Workout User'],
        responses={200: "Workouts for the week"}
    )
    @action(detail=False, methods=['get'], url_path="workouts-for-week")
    def workouts_for_week(self, request):
        date_str = request.query_params.get('date_str')
        if not date_str:
            return Response({"error": "Missing 'date_str' query parameter"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convertir la chaîne de date en objet datetime
            date = make_aware(datetime.strptime(date_str, '%Y-%m-%d'))
            start_week = date - timedelta(days=date.weekday())  # Lundi de la semaine
            end_week = start_week + timedelta(days=7)  # Dimanche de la semaine

            # Filtrer les Workouts pour l'utilisateur connecté et la semaine en cours
            workouts = Workout.objects.filter(
                date__date__gte=start_week.date(),
                date__date__lt=end_week.date(),
                user=request.user
            ).values('date__date').annotate(count=Count('id'))

            # Construire la réponse avec les jours de la semaine
            week_workouts = {str(day['date__date']): True for day in workouts}
            for i in range(7):
                current_day = (start_week + timedelta(days=i)).date()
                if str(current_day) not in week_workouts:
                    week_workouts[str(current_day)] = False

            return Response(week_workouts, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @extend_schema(
        tags=['Workout User'],
        responses={200: "Workouts for the month"}
    )
    @action(detail=False, methods=['get'], url_path="workouts-for-month")
    def workouts_for_month(self, request):
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        if not year or not month:
            return Response({"error": "Missing 'year' or 'month' query parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            year = int(year)
            month = int(month)

            # Définir la date de début du mois précédent, mois actuel et mois suivant
            start_current_month = make_aware(datetime(year, month, 1))
            start_previous_month = (start_current_month - timedelta(days=1)).replace(day=1)
            start_next_month = (start_current_month + timedelta(days=32)).replace(day=1)

            # Définir la date de fin pour les trois mois
            end_next_month = (start_next_month + timedelta(days=31)).replace(day=1)

            # Filtrer les Workouts pour l'utilisateur connecté et les mois sélectionnés
            workouts = Workout.objects.filter(
                date__date__gte=start_previous_month,
                date__date__lt=end_next_month,
                user=request.user
            ).values('date__date').annotate(count=Count('id'))

            # Construire la réponse avec les jours des trois mois
            all_workouts = {str(day['date__date']): True for day in workouts}

            def add_month_days(year, month):
                start_date = datetime(year, month, 1)
                if month == 12:
                    end_date = datetime(year + 1, 1, 1)
                else:
                    end_date = datetime(year, month + 1, 1)
                total_days_in_month = (end_date - start_date).days
                for day in range(1, total_days_in_month + 1):
                    current_day = f"{year}-{month:02d}-{day:02d}"
                    if current_day not in all_workouts:
                        all_workouts[current_day] = False

            # Ajouter les jours pour le mois précédent, le mois courant et le mois suivant
            if month == 1:
                add_month_days(year - 1, 12)
            else:
                add_month_days(year, month - 1)
            
            add_month_days(year, month)

            if month == 12:
                add_month_days(year + 1, 1)
            else:
                add_month_days(year, month + 1)

            return Response(all_workouts, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

