from rest_framework import serializers
from escola.models import Aluno, Curso


class alunoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class cursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'