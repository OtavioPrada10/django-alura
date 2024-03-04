from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class alunoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class cursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class matriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = []

class listaMatriculasAluno(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

class ListaAlunosMatriculadosEmUmCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='alunos.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']