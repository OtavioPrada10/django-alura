from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import (AlunosViewSet, CursosViewSet, ListaAlunosMatriculados,listaMatriculasAluno, MatriculaViewSet)
from django.contrib import admin

router = DefaultRouter()
router.register(r'alunos', AlunosViewSet, basename='Alunos')
router.register(r'cursos', CursosViewSet, basename='Cursos')
router.register(r'matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', listaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]