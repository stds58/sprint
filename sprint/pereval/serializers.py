from .models import User, PerevalAdded, Coord, Level, PerevalImages
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']


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


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    user = UsersSerializer()
    coord = CoordSerializer()
    level = LevelSerializer()
    images = PerevalImagesSerializer(many=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = PerevalAdded
        depth = 1
        fields = ['id', 'beauty_title', 'title', 'other_title', 'connect', 'add_time', 'status', 'user', 'coord', 'level', 'images']

    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        coord = validated_data.pop('coord')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        user = User.objects.update(**user)
        coord = Coord.objects.update(**coord)
        level = Level.objects.update(**level)

        for image in images:
            data = image.pop('img')
            title = image.pop('title')
            PerevalImages.objects.update(img=data, title=title)

        return super().update(instance, validated_data)


    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coord = validated_data.pop('coord')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        user, created = User.objects.get_or_create(**user)

        coord = Coord.objects.create(**coord)
        level = Level.objects.create(**level)
        pereval = PerevalAdded.objects.create(**validated_data, user=user, coord=coord, level=level, status='new')

        for image in images:
            data = image.pop('img')
            title = image.pop('title')
            PerevalImages.objects.create(img=data, perevaladded=pereval, title=title)

        return pereval


    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = [
                instance_user.name != data_user['name'],
                instance_user.fam != data_user['fam'],
                instance_user.otc != data_user['otc'],
                instance_user.phone != data_user['phone'],
                instance_user.email != data_user['email'],
            ]
            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'отклонено':'у пользователя нельзя изменить данные'})
        return data








