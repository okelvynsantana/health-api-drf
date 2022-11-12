from django.db import models
from history.models import History
from patient.models import Patient


def history_images(instance, filename):
    print(instance)
    return '/'.join(['history', str(instance.history_id.id_patient), filename])


def patient_images(instance, filename):
    print(instance)
    return '/'.join(['patient', str(instance.patient_id.id_patient), filename])


class HistoryImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(blank=True, null=True, upload_to=history_images)
    history_id = models.ForeignKey(History, related_name='images', on_delete=models.CASCADE, blank=False, null=False)


class PatientImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(blank=True, null=True, upload_to=patient_images)
    patient_id = models.ForeignKey(Patient, related_name='images', on_delete=models.CASCADE, blank=False, null=False)
