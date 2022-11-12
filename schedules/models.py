from django.db import models
from patient.models import Patient

class Schedule(models.Model):
    id_schedule = models.AutoField(primary_key=True)
    schedule_datetime = models.DateTimeField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    canceled = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    schedule_type = models.CharField(max_length=100, blank=True, null=True)
    patient_id = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='schedules',
        blank=False,
        null=False
    )

    class Meta:
        managed = True
        db_table = 'schedules'
        unique_together = ('schedule_datetime', 'patient_id')
