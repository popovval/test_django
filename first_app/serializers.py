from rest_framework import serializers
from .models import FirstObj


class FirstObjSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FirstObj
        fields = ('column_num', 'column_char')
