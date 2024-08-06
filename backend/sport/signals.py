from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import RecordsGroupSport, RecordsSport

@receiver(pre_delete, sender=RecordsGroupSport)
def handle_records_on_group_deletion(sender, instance, **kwargs):
    # Récupérer le groupe général pour le même sport
    general_group = RecordsGroupSport.objects.filter(is_general=True, sport=instance.sport).first()

    # Mettre à jour tous les records qui appartiennent à ce groupe pour les assigner au groupe général
    if general_group:
        RecordsSport.objects.filter(groups=instance).update(groups=general_group)
    else:
        # Si aucun groupe général n'existe, supprimer la référence au groupe
        RecordsSport.objects.filter(groups=instance).update(groups=None)