from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from .serializer import alunoSerializer, cursoSerializer, matriculaSerializer, listaMatriculasAluno

class alunosViewSet(viewsets.ModelViewSet):    
    """
    Exibindo todos os registros da tabela alunos
    """
    queryset = Aluno.objects.all()
    serializer_class = alunoSerializer

class cursosViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all()
    serializer_class = cursoSerializer

class matriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = matriculaSerializer

class listaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno"""
    serializer_class = listaMatriculasAluno
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        # return super().get_queryset()