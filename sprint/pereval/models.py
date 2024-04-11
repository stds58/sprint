from django.db import models



class User(models.Model):
    name = models.CharField(max_length=255, default="")
    fam = models.CharField(max_length=255, default="")
    otc = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, unique=True, default="") #, unique=True

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'fam', 'otc', 'phone']


class PerevalAdded(models.Model):
    CHOICE_STATUS = (
        ("new", 'новый'),
        ("pending", 'модератор взял в работу'),
        ("accepted", 'модерация прошла успешно'),
        ("rejected", 'модерация прошла, информация не принята'),
    )
    CHOICE_ACTIVITIES = (
        (1, 'пешком'),
        (2, 'лыжи'),
        (3, 'катамаран'),
        (4, 'байдарка'),
        (5, 'плот'),
        (6, 'сплав'),
        (7, 'велосипед'),
        (8, 'автомобиль'),
        (9, 'мотоцикл'),
        (10, 'парус'),
        (11, 'верхом')
    )
    beauty_title = models.CharField(max_length=255, default="")
    title = models.CharField(max_length=255, default="")
    other_title = models.CharField(max_length=255, default="")
    connect = models.TextField(default="")
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICE_STATUS, default="new")
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='users')
    coord = models.ForeignKey('Coord', on_delete=models.CASCADE, related_name='coord')
    level = models.ForeignKey('Level', on_delete=models.CASCADE, related_name='level')
    spr_activities_types = models.IntegerField(choices=CHOICE_STATUS, default=1)


class Coord(models.Model):
    latitude = models.DecimalField(decimal_places=8, max_digits=10, default=1.2)
    longitude = models.DecimalField(decimal_places=8, max_digits=10, default=1.2)
    height = models.IntegerField(default=0)


class Level(models.Model):
    CHOICE_LEVEL = (
        ('1A', '1A'),
        ('2A', '2A'),
        ('3A', '3A'),
        ('4A', '4A'),
    )
    winter = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")
    summer = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")
    autumn = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")
    spring = models.CharField(max_length=2, choices=CHOICE_LEVEL, default="1A")


class PerevalImages(models.Model):
    perevaladded = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=255, default="")
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images', blank=True, unique=True)







