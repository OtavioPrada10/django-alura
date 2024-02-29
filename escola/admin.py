from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('name',)
    list_per_pag = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso', )
    search_fields = ('name',)

admin.site.register(Curso, Cursos)