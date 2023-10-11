from rest_framework import serializers
from .models import Agenda




class AgendaSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Agenda
        fields = "__all__"



## define validators



