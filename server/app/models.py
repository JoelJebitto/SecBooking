from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

# Signal to create or update a user's profile whenever the user is created or updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Exam(models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField()
    date_time = models.DateTimeField()
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_student')

class Class(models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField()
    date_time = models.DateTimeField()
    students = models.ManyToManyField(User, related_name='classes')

class AnswerSheet(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_sheets')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='answer_sheets')
    pdf = models.FileField(upload_to='answersheets/')  # PDF field
