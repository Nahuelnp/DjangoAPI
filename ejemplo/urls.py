from django.urls import path, include
from rest_framework import routers
from .viewsets import TaskViewSet
from . import views


router = routers.SimpleRouter()
router.register('tasks',TaskViewSet)


urlpatterns = router.urls
