from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import alunosViewSet, cursosViewSet

router = DefaultRouter()
router.register(r'alunos', alunosViewSet)
router.register(r'cursos', cursosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]