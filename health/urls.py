from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from patient.api.viewsets import PatientsViewSets
from schedules.api.viewsets import ScheduleViewSet
from history.api.viewsets import HistoryViewSets
from images.api.viewsets import ImageHistoryViewSet, PatientImageViewSet


router = routers.DefaultRouter()
router.register(r'patients', PatientsViewSets)
router.register(r'schedules', ScheduleViewSet)
router.register(r'histories', HistoryViewSets)
router.register(r'history_images', ImageHistoryViewSet)
router.register(r'patient_images', PatientImageViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

