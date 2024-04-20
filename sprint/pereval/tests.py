from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import PerevalSerializer
from .models import User, PerevalAdded, Coord, Level, PerevalImages


class PassTestCase(APITestCase):

    def setUp(self):
        # Объект перевал 1
        self.pass_1 = PerevalAdded.objects.create(
            user=User.objects.create(
                email='Ivanov@mail.ru',
                fam='Иванов',
                name = 'Петр',
                otc = 'Васильевич',
                phone='89999999999'
            ),
            beauty_title='beauty_title',
            title='title',
            other_title='other_title',
            connect='connect',
            coord=Coord.objects.create(
                latitude=22.222,
                longitude=11.111,
                height=1000
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )

        # Изображение для объекта перевал 1
        self.image_1 = PerevalImages.objects.create(
            title='Title_1',
            img='https://images.gl/eTdfdfgk33vNQG8',
            perevaladded=self.pass_1
        )

        # Объект перевал 2
        self.pass_2 = PerevalAdded.objects.create(
            user=User.objects.create(
                email='Petrov@mail.ru',
                fam='Петров',
                name='Иван',
                otc='Васильевич',
                phone='89999998877'
            ),
            beauty_title='beauty_title2',
            title='title2',
            other_title='other_title2',
            connect='connect2',
            coord=Coord.objects.create(
                latitude=11.222,
                longitude=22.111,
                height=2000
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )

        # Изображение для объекта перевал 2
        self.image_2 = PerevalImages.objects.create(
            title='Title_2',
            img='https://images.gl/8JQjhxTuFYCcRG7',
            perevaladded=self.pass_2
        )

    def test_pereval_list(self):
        """Тест endpoint /api/Pereval/ - список всех объектов модели PerevalAdded"""
        response = self.client.get('/api/Pereval/')
        serializer_data = PerevalSerializer([self.pass_1, self.pass_2], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(serializer_data, response.data)

    def test_pereval_detail(self):
        """Тест endpoint /api/Pereval - объект модели Pass по его id"""

        response = self.client.get(f'/api/Pereval/{self.pass_1.id}/')
        serializer_data = PerevalSerializer(self.pass_1).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_pereval_user_email(self):
        """Тест endpoint /api/Pereval/user__email=<email> - объекты модели Pass отфильтрованные по email пользователя"""

        email = self.pass_1.user.email
        url = f'/api/Pereval/?user__email={email}'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)