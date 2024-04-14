# Generated by Django 4.0.10 on 2024-04-14 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0003_rename_users_perevaladded_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coord',
            name='latitude',
            field=models.DecimalField(decimal_places=8, default=1.2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='coord',
            name='longitude',
            field=models.DecimalField(decimal_places=8, default=1.2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='beauty_title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='connect',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='pereval.level'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='other_title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='spr_activities_types',
            field=models.IntegerField(choices=[(1, 'пешком'), (2, 'лыжи'), (3, 'катамаран'), (4, 'байдарка'), (5, 'плот'), (6, 'сплав'), (7, 'велосипед'), (8, 'автомобиль'), (9, 'мотоцикл'), (10, 'парус'), (11, 'верхом')], default=1),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='perevalimages',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='fam',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='otc',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=255),
        ),
    ]
