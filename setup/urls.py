from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import alunosViewSet, cursosViewSet, listaMatriculasAluno, matriculaViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'alunos', alunosViewSet, basename='Alunos')
router.register(r'cursos', cursosViewSet, basename='Cursos')
router.register(r'matriculas', matriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas', listaMatriculasAluno.as_view())
]