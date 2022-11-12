from django.db import models


class Patient(models.Model):
    id_patient = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    address_number = models.IntegerField(blank=True, null=True)
    neighborhood = models.CharField(max_length=60, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    document = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "patients"
