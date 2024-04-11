from .models import User, PerevalAdded, Coord, Level, PerevalImages
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


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
    img = serializers.URLField()
    class Meta:
        model = PerevalImages
        fields = ['title', 'img']


class PerSerializer(WritableNestedModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['beauty_title', 'title', 'other_title', 'connect', 'add_time', 'images']


class PerevalSerializer(WritableNestedModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['beauty_title', 'title', 'other_title', 'connect', 'add_time', 'images', 'user', 'coord', 'level']

    user = UsersSerializer()
    coord = CoordSerializer()
    level = LevelSerializer()
    images = PerevalImagesSerializer(many=True)





