from django.contrib import admin
from .models import *
# Register your models here.


# admin.register() decorator
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'servico', 'descricao_servico')


#admin.site.register(Servico)
@admin.register(Postagem)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_criacao', 'autor_postagem', 'data_postagem', 'titulo', 'tags', 'texto' )


@admin.register(IntegranteEquipe)
class IntegranteEquipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'expertise', 'equipe_servico')

#admin.site.unregister(Grupo)


admin.site.site_header = "Painel Administrativo - Cronos API"




""" class ResourceAdmin(admin.ModelAdmin):
    def delete(self, obj):
        return '< input onclick="location.href=\'%s/delete/\'" type="button" value="Delete" />'.format(obj.pk)

    delete.allow_tags = True
    delete.short_description = 'Delete object'

    list_display = ('delete') """