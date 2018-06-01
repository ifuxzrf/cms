from display_section.models import Things
from rest_framework import serializers


class ThingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Things
        fields = ('name', 'price')


