from django.db import models
from schedules.models import Schedule


class History(models.Model):
    id_history = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    onset_of_symptoms = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    pain_local = models.CharField(max_length=100, blank=True, null=True)
    pain_type = models.CharField(max_length=100, blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)
    schedule_id = models.ForeignKey(
        Schedule, on_delete=models.CASCADE,
        related_name='histories',
        blank=False,
        null=False
    )

    class Meta:
        managed = True,
        db_table = 'histories'

