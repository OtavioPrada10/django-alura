from rest_framework import viewsets
from escola.models import Aluno, Curso
from .serializer import alunoSerializer, cursoSerializer

class alunosViewSet(viewsets.ModelViewSet):    
    """
    Exibindo todos os registros da tabela alunos
    """
    queryset = Aluno.objects.all()
    serializer_class = alunoSerializer

class cursosViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all()
    serializer_class = cursoSerializer