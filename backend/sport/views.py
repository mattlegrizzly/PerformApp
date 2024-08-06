from rest_framework import permissions, viewsets
from .models import Sport, SportsUser, RecordsGroupSport
from .serializers import SportSerializer, SportsUserSerializer, SportsDetailedUserSerializer, RecordsSportUser, RecordsSport, RecordsSportDetailedUserSerializer, RecordsSportSerializer, RecordsSportUserSerializer, RecordsGroupSportSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from users2.permissions import IsUserOrAdmin
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import filters, mixins, status, pagination
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
from utils.utils import get_ordered_queryset

class SportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

    def get_queryset(self):
        """ # Si l'action en cours est 'retrieve', retourner un queryset sans filtre
        if self.action == 'retrieve':
            return Sport.objects.all() """

        queryset = Sport.objects.filter(isTheme=False).all()
        return queryset
    
    @action(detail=False, methods=['get'], url_path="all")
    def all(self, request):
        queryset = self.get_queryset()
        queryset = get_ordered_queryset(self.get_queryset(), request.query_params)
        queryset = self.get_serializer(queryset, many=True)
        return Response(queryset.data)

class SportsUserViewSet(viewsets.ModelViewSet):
    queryset = SportsUser.objects.all()
    serializer_class = SportsUserSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsUserOrAdmin]
        return [permission() for permission in permission_classes]

    @extend_schema(
        tags=['Sports User'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Sports User'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_sports_user = self.get_latest()
        serializer = self.serializer_class(latest_sports_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Sports User'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SportsDetailedUserSerializer(instance)
        return Response(serializer.data)

    @extend_schema(
        tags=['Sports User'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        sport_id = request.data.get('sport')
        
        if self.queryset.filter(user=user_id, sport=sport_id).exists():
            raise ValidationError("An entry with this user and sport already exists.")

        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Sports User'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Sports User'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Sports User'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
class RecordsSportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RecordsSport.objects.all().order_by('order')
    serializer_class = RecordsSportSerializer

    @extend_schema(
        tags=['Records Sport'],
        responses={200: RecordsSportSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path="all")
    def all(self, request):
        queryset = self.get_queryset()
        records_by_sport = {}
        
        for record in queryset:
            sport_name = record.sport.name
            if sport_name not in records_by_sport:
                records_by_sport[sport_name] = []
            records_by_sport[sport_name].append(self.get_serializer(record).data)
        
        return Response(records_by_sport)
    
    @extend_schema(
        tags=['Records Sport'],
        responses={200: RecordsSportSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Records Sport'],
        responses={200: RecordsSportSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path="by-sport")
    def by_sport(self, request):
        sport_id = request.query_params.get('sport_id')
        if not sport_id:
            return Response({"detail": "sport_id query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset().filter(sport_id=sport_id).all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecordsGroupsSportViewSet(viewsets.ModelViewSet):
    queryset = RecordsGroupSport.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RecordsGroupSportSerializer
        return RecordsGroupSportSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    @extend_schema(
        tags=['Records Sport User'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Record Groups'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_records_user = self.queryset.order_by('-created_at')[:1]  # Example logic for latest
        serializer = self.get_serializer(latest_records_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Record Groups'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @extend_schema(
        tags=['Record Groups'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Record Groups'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Record Groups'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Record Groups'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Record Groups'],
        responses={200: RecordsSportSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path="by-sport")
    def by_sport(self, request):
        sport_id = request.query_params.get('sport_id')
        if not sport_id:
            return Response({"detail": "sport_id query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset().filter(sport_id=sport_id).all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecordsSportUserViewSet(viewsets.ModelViewSet):
    queryset = RecordsSportUser.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RecordsSportDetailedUserSerializer
        return RecordsSportUserSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsUserOrAdmin]
        return [permission() for permission in permission_classes]

    @extend_schema(
        tags=['Records Sport User'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Records Sport User'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_records_user = self.queryset.order_by('-created_at')[:1]  # Example logic for latest
        serializer = self.get_serializer(latest_records_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Records Sport User'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @extend_schema(
        tags=['Records Sport User'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Records Sport User'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Records Sport User'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Records Sport User'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        tags=['Records Sport User'],
        responses={200: RecordsSportUserSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path="by-theme-sports")
    def by_theme_sports(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"detail": "user_id query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        theme_sports = Sport.objects.filter(isTheme=True).values_list('id', flat=True)

        all_records = RecordsSport.objects.filter(sport_id__in=theme_sports).order_by('sport__name', 'groups__is_general', 'groups__name', 'order')
        user_records = self.get_queryset().filter(user_id=user_id, record__sport_id__in=theme_sports)

        latest_user_records = {}
        for record in user_records:
            key = (record.record.sport.name, record.record.id)
            if key not in latest_user_records or record.date_record > latest_user_records[key].date_record:
                latest_user_records[key] = record

        records_by_sport = {}
        for record in all_records:
            sport_name = record.sport.name
            group_name = record.groups.name if record.groups else "General"

            if sport_name not in records_by_sport:
                records_by_sport[sport_name] = {}
            if group_name not in records_by_sport[sport_name]:
                records_by_sport[sport_name][group_name] = []

            key = (sport_name, record.id)
            if key in latest_user_records:
                latest_record = latest_user_records[key]
                record_data = self.get_serializer(latest_record).data
                record_data['record_name'] = latest_record.record.name
                record_data['units'] = latest_record.record.units
                record_data['formatted_record'] = format_record(latest_record)
                records_by_sport[sport_name][group_name].append(record_data)
            else:
                empty_record_data = {
                    'id': None,
                    'record': record.id,
                    'record_name': record.name,
                    'units': record.units,
                    'user': user_id,
                    'time_value': '',
                    'record_value': '',
                    'free_value': '',
                    'formatted_record': '' if record.units == 'time' else '',
                    'created_at': None,
                    'updated_at': None,
                    'date_record': None
                }
                records_by_sport[sport_name][group_name].append(empty_record_data)

        return Response(records_by_sport, status=status.HTTP_200_OK)
    
    @extend_schema(
    tags=['Records Sport User'],
    responses={200: RecordsSportUserSerializer(many=True)}
    )      
    @action(detail=False, methods=['get'], url_path="by-user-sports")
    def by_user_sports(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"detail": "user_id query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        user_sports = SportsUser.objects.filter(user_id=user_id).values_list('sport_id', flat=True)

        all_records = RecordsSport.objects.filter(sport_id__in=user_sports).order_by('sport__name', 'groups__is_general', 'groups__name', 'order')
        user_records = self.get_queryset().filter(user_id=user_id, record__sport_id__in=user_sports)

        latest_user_records = {}
        for record in user_records:
            key = (record.record.sport.name, record.record.id)
            if key not in latest_user_records or record.date_record > latest_user_records[key].date_record:
                latest_user_records[key] = record

        records_by_sport = {}
        for record in all_records:
            sport_name = record.sport.name
            group_name = record.groups.name if record.groups else "General"

            if sport_name not in records_by_sport:
                records_by_sport[sport_name] = {}
            if group_name not in records_by_sport[sport_name]:
                records_by_sport[sport_name][group_name] = []

            key = (sport_name, record.id)
            if key in latest_user_records:
                latest_record = latest_user_records[key]
                record_data = self.get_serializer(latest_record).data
                record_data['record_name'] = latest_record.record.name
                record_data['units'] = latest_record.record.units
                record_data['formatted_record'] = format_record(latest_record)
                records_by_sport[sport_name][group_name].append(record_data)
            else:
                empty_record_data = {
                    'id': None,
                    'record': record.id,
                    'record_name': record.name,
                    'units': record.units,
                    'user': user_id,
                    'time_value': '',
                    'record_value': '',
                    'free_value': '',
                    'formatted_record': '' if record.units == 'time' else '',
                    'created_at': None,
                    'updated_at': None,
                    'date_record': None
                }
                records_by_sport[sport_name][group_name].append(empty_record_data)

        return Response(records_by_sport, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Records Sport User'],
        responses={200: RecordsSportUserSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path="by-record")
    def by_record(self, request):
        record_id = request.query_params.get('record_id')
        if not record_id:
            return Response({"detail": "record_id query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            record = RecordsSport.objects.get(id=record_id)
        except RecordsSport.DoesNotExist:
            return Response({"detail": "Record not found."}, status=status.HTTP_404_NOT_FOUND)

        user_records = self.get_queryset().filter(record_id=record_id).order_by('date_record')
        performances = []

        for user_record in user_records:
            record_data = self.get_serializer(user_record).data
            if record.units == 'time':
                formatted_time = user_record.formatted_time_value()
                record_data['formatted_record'] = formatted_time if formatted_time else ''
            elif record.units == 'weight':
                record_data['formatted_record'] = f"{user_record.formatted_record_value()} kg" if user_record.formatted_record_value() else ''
            elif record.units == 'points' or record.units =='reps':
                record_data['formatted_record'] = f"{user_record.formatted_record_value()}" if user_record.formatted_record_value() else ''
            elif record.units == 'distance_m':
                record_data['formatted_record'] = f"{user_record.formatted_record_value()} m" if user_record.formatted_record_value() else ''
            elif record.units == 'distance_km':
                record_data['formatted_record'] = f"{user_record.formatted_record_value()} km" if user_record.formatted_record_value() else ''
            elif record.units == 'free':
                    record_data['formatted_record'] = f"{user_record.free_value}" if user_record.free_value else ''
            performances.append(record_data)

        response_data = {
            'record_name': record.name,
            'units': record.units,
            'performances': performances
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
def format_record(record):
    if record.record.units == 'time':
        return record.formatted_time_value() or ''
    elif record.record.units == 'weight':
        return f"{record.formatted_record_value()} kg" if record.formatted_record_value() else ''
    elif record.record.units == 'points' or record.record.units == 'reps' :
        return f"{record.formatted_record_value()}" if record.formatted_record_value() else ''
    elif record.record.units == 'distance_m':
        return f"{record.formatted_record_value()} m" if record.formatted_record_value() else ''
    elif record.record.units == 'distance_km':
        return f"{record.formatted_record_value()} km" if record.formatted_record_value() else ''
    elif record.record.units == 'free':
        return record.free_value or ''
    return ''