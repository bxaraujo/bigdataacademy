from rest_framework import serializers
from .models import Postagem, Servico, IntegranteEquipe



class IntegranteEquipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntegranteEquipe
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['equipe_servico'] = ServicoSerializer(instance.equipe_servico).data['servico']
        return rep

class PostagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Postagem
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['autor_postagem'] = IntegranteEquipeSerializer(instance.autor_postagem).data['nome']
        return rep


class ServicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servico
        fields = '__all__'

