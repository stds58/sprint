from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .serializers import *



class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
#

class CoordViewset(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer

#
# class LevelViewset(viewsets.ModelViewSet):
#     queryset = Level.objects.all()
#     serializer_class = LevelSerializer
#
#
# class PerevalImageViewset(viewsets.ModelViewSet):
#     queryset = PerevalImages.objects.all()
#     serializer_class = PerevalImagesSerializer


class PerevalViewset(viewsets.ModelViewSet):
    #queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer


    @action(detail=False, methods=['post'])
    def submitData(self, request):
        #print('request', dir(request.data))
        #data = request.data
        print('request.data', request.data)
        #print('data.keys', request.data.lists)
        # print('data.pop', request.data.pop)
        # udata = UsersSerializer(data=request.data)
        # print('udata',udata)
        user_serializer = UsersSerializer(data=request.data)
        coords_serializer = CoordSerializer(data=request.data)
        level_serializer = LevelSerializer(data=request.data)
        images_serializers = PerevalImagesSerializer(data=request.data)
        pereval_serializer = PerSerializer(data=request.data)
        #print('user_serializer',user_serializer)
        # print('coords_serializer', coords_serializer)
        #print('level_serializer', level_serializer)
        #print('images_serializers', images_serializers)
        # images_serializers = [PerevalImagesSerializer(data=image_data) for image_data in images_data]
        user_serializer.is_valid()
        coords_serializer.is_valid()
        level_serializer.is_valid()
        images_serializers.is_valid()
        pereval_serializer.is_valid()

        if pereval_serializer.is_valid() and user_serializer.is_valid() and coords_serializer.is_valid() and level_serializer.is_valid() and images_serializers.is_valid():
            # all(image_serializer.is_valid() for image_serializer in images_serializers):
            # user_instance = user_serializer.save()
            # print('coords_serializer', coords_serializer)
            # coords_instance = coords_serializer.save()
            # level_instance = level_serializer.save()
            # pereval_instance = pereval_serializer.save()
            #
            # for image_serializer in images_serializers:
            #     image_serializer.save(pereval=pereval_instance)

            return Response({'status': 200, 'message': 'Отправлено успешно', 'id': 0}, #pereval_instance.id
                            status=status.HTTP_200_OK)

        else:
            print('u',user_serializer.is_valid() )
            print('c',coords_serializer.is_valid() )
            print('l',level_serializer.is_valid() )
            print('i',images_serializers.is_valid() )
            print('p', pereval_serializer.is_valid())
            return Response({'status': 400, 'message': 'Bad Request, недостаточно полей', 'id': None},
                            status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     # level_data = data.get('level')
        #     # user_data = data.get('user')
        #     # coords_data = data.get('coord')
        #     # images_data = data.get('images1')
        #
        #     user_serializer = UsersSerializer(data=request.data).is_valid()
        #     coords_serializer = CoordSerializer(data=request.data).is_valid()
        #     level_serializer = LevelSerializer(data=request.data).is_valid()
        #     images_serializers = PerevalImagesSerializer(data=request.data).is_valid()
        #     #images_serializers = [PerevalImagesSerializer(data=image_data) for image_data in images_data]
        #
        #     if user_serializer.is_valid() and coords_serializer.is_valid() and level_serializer.is_valid() and image_serializer.is_valid():
        #             #all(image_serializer.is_valid() for image_serializer in images_serializers):
        #         user_instance = user_serializer.save()
        #         print('user_instance', user_instance)
        #         coords_instance = coords_serializer.save()
        #         level_instance = level_serializer.save()
        #
        #         pereval_data = {
        #             'user': user_instance.id,
        #             'coords': coords_instance.id,
        #             'level': level_instance.id,
        #             **data  # Remaining data
        #         }
        #
        #         pereval_serializer = PerevalSerializer(data=pereval_data)
        #         if pereval_serializer.is_valid():
        #             pereval_instance = pereval_serializer.save()
        #
        #             for image_serializer in images_serializers:
        #                 image_serializer.save(pereval=pereval_instance)
        #
        #             return Response({'status': 200, 'message': 'Отправлено успешно', 'id': pereval_instance.id},
        #                             status=status.HTTP_200_OK)
        #     else:
        #         return Response({'status': 400, 'message': 'Bad Request, недостаточно полей', 'id': None},
        #                         status=status.HTTP_400_BAD_REQUEST)
        #
        # except Exception as e:
        #     print('Exception')
        #     return Response({'status': 500, 'message': str(e), 'id': None},
        #                     status=status.HTTP_500_INTERNAL_SERVER_ERROR)