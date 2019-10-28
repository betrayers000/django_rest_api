# Generated by Django 2.2.6 on 2019-10-28 06:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.TextField()),
                ('email', models.CharField(max_length=100, validators=[django.core.validators.EmailValidator(message='이메일 형식을 넣어주세요')])),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(20, message='미성년자는 가입할수 없습니다.')])),
            ],
        ),
    ]
