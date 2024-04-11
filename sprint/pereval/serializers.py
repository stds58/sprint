from .models import User, PerevalAdded, Coord, Level, PerevalImages
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'fam', 'otc', 'phone', 'email']


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class PerevalImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerevalImages
        fields = ['title', 'img']


class PerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['beauty_title', 'title', 'other_title', 'connect', 'add_time']


class PerevalSerializer(serializers.Serializer):
    user = UsersSerializer()
    coord = CoordSerializer()
    level = LevelSerializer()
    images1 = PerevalImagesSerializer() #many=True
    #images2 = PerevalImagesSerializer()
    pereval = PerSerializer()
