from django.db import models
from sport.models import Sport
from typing import List
from datetime import datetime
from moviepy.editor import VideoFileClip
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO

def upload_to_video(instance, filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    ext = filename.split('.')[-1]  # Récupérer l'extension du fichier
    filename_edit = f'exercice_{instance.name.replace(" ", "_")}_{timestamp}.{ext}'
    return 'video/{filename}'.format(filename=filename_edit)

def upload_to_thumbnail(instance, filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename_edit = f'exercice_{instance.name.replace(" ", "_")}_{timestamp}.jpg'
    image_path = f'video/thumbnails/{filename_edit}'
    
    return image_path

def generate_thumbnail(instance):
    # Path where the video is saved
    video_path = instance.video.path

    if (video_path):
        # Extract the thumbnail from the video
        clip = VideoFileClip(video_path)
        frame = clip.get_frame(1.0)  # Get frame at 1 second
        
        # Save the frame as an image
        image_filename = upload_to_thumbnail(instance, instance.video.name)
        image = Image.fromarray(frame)
        buffer = BytesIO()
        image.save(buffer, format="JPEG")
        buffer.seek(0)
        
        # Save the image to the instance
        instance.thumbnail.save(image_filename, ContentFile(buffer.read()), save=False)
        
        # Clean up the clip
        clip.reader.close()
        if clip.audio:
            clip.audio.reader.close_proc()

def upload_to(instance, filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    ext = filename.split('.')[-1]  # Récupérer l'extension du fichier
    filename_edit = f"material_{instance.id}_{timestamp}.{ext}"
    return 'images/{filename}'.format(filename=filename_edit)

class Zone(models.TextChoices):
    muscle = 'MU', "Muscle"
    articulation = 'AR', "Articulation"

class WorkZone(models.Model):
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=100, null=False, primary_key=True)
    zone = models.CharField(choices=Zone.choices , default=Zone.muscle, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def getZone(self) -> Zone:
        # Get value from choices enum
        return self.zone(self.zone)

class Material(models.Model):
    name = models.CharField(max_length=100)
    pictures = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to=upload_to_video, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    materials = models.ManyToManyField(to=Material, through="exercise.ExerciseMaterial")
    sports = models.ManyToManyField(to=Sport, through="exercise.ExerciseSport")
    muscles = models.ManyToManyField(to=WorkZone, through="exercise.ExerciseZone")
    thumbnail = models.ImageField(upload_to=upload_to_thumbnail, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Supprimer l'ancienne vidéo et vignette si elles existent
        if self.pk:  # Si l'objet existe déjà (mise à jour)
            old_instance = self.__class__.objects.get(pk=self.pk)
            if old_instance.video and old_instance.video.name != self.video.name:
                old_instance.video.delete(save=False)
            if old_instance.thumbnail and old_instance.thumbnail.name != self.thumbnail.name:
                old_instance.thumbnail.delete(save=False)
        
        # Appel de la fonction pour sauvegarder la vidéo
        super(Exercise, self).save(*args, **kwargs)
        
        # Générer la vignette après avoir sauvegardé la vidéo
        if self.video and not self.thumbnail:
            generate_thumbnail(self)
            super(Exercise, self).save(update_fields=['thumbnail'])

    @property
    def material_ids(self) -> List[int]:
        return [material.id for material in self.materials.all()]
    
    @property
    def sports_ids(self) -> List[int]:
        return [sport.id for sport in self.sports.all()]
    
    @property
    def muscles_ids(self) -> List[str]:
        return [muscle.code for muscle in self.muscles.all()]

class ExerciseStep(models.Model):
    text = models.CharField(max_length=255)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="steps_exercise")

class ExerciseMaterial(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="material_exercise")

class ExerciseSport(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sports_exercise')

class ExerciseZone(models.Model):
    zone = models.ForeignKey(WorkZone, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="zone_exercises")
