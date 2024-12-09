# Generated by Django 5.1.3 on 2024-12-05 05:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieCd', models.IntegerField(help_text='영화 ID', primary_key=True, serialize=False)),
                ('movieNm', models.CharField(help_text='영화명(국문)을 출력합니다.', max_length=255)),
                ('movieNmEn', models.CharField(blank=True, help_text='영화명(영문)을 출력합니다.', max_length=255, null=True)),
                ('movieNmOg', models.CharField(blank=True, help_text='영화명(원문)을 출력합니다.', max_length=255, null=True)),
                ('prdtYear', models.CharField(help_text='제작연도를 출력합니다.', max_length=4)),
                ('showTm', models.CharField(help_text='상영시간을 출력합니다.', max_length=10)),
                ('openDt', models.CharField(help_text='개봉연도를 출력합니다.', max_length=10)),
                ('prdtStatNm', models.CharField(help_text='제작상태명을 출력합니다.', max_length=100)),
                ('typeNm', models.CharField(help_text='영화유형명을 출력합니다.', max_length=100)),
                ('nations', models.CharField(help_text='제작국가를 나타냅니다.', max_length=255)),
                ('nationNm', models.CharField(help_text='제작국가명을 출력합니다.', max_length=255)),
                ('genreNm', models.CharField(help_text='장르명을 출력합니다.', max_length=255)),
                ('showTypes', models.CharField(help_text='상영형태 구분을 나타냅니다.', max_length=100)),
                ('showTypeGroupNm', models.CharField(help_text='상영형태 구분을 출력합니다.', max_length=100)),
                ('showTypeNm', models.CharField(help_text='상영형태명을 출력합니다.', max_length=100)),
                ('audits', models.CharField(help_text='심의정보를 나타냅니다.', max_length=255)),
                ('auditNo', models.CharField(help_text='심의번호를 출력합니다.', max_length=100)),
                ('watchGradeNm', models.CharField(help_text='관람등급 명칭을 출력합니다.', max_length=100)),
                ('staffs', models.CharField(help_text='스텝을 나타냅니다.', max_length=255)),
                ('tmdb_movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kobis_movie', to='tmdb.tmdbmovie')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peopleNm', models.CharField(help_text='감독명을 출력합니다.', max_length=255)),
                ('peopleNmEn', models.CharField(blank=True, help_text='감독명(영문)을 출력합니다.', max_length=255, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directors', to='kobis.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCd', models.CharField(help_text='참여 영화사 코드를 출력합니다.', max_length=100)),
                ('companyNm', models.CharField(help_text='참여 영화사명을 출력합니다.', max_length=255)),
                ('companyNmEn', models.CharField(blank=True, help_text='참여 영화사명(영문)을 출력합니다.', max_length=255, null=True)),
                ('companyPartNm', models.CharField(help_text='참여 영화사 분야명을 출력합니다.', max_length=255)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='kobis.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peopleNm', models.CharField(help_text='배우명을 출력합니다.', max_length=255)),
                ('peopleNmEn', models.CharField(blank=True, help_text='배우명(영문)을 출력합니다.', max_length=255, null=True)),
                ('cast', models.CharField(help_text='배역명을 출력합니다.', max_length=255)),
                ('castEn', models.CharField(blank=True, help_text='배역명(영문)을 출력합니다.', max_length=255, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actors', to='kobis.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peopleNm', models.CharField(help_text='스텝명을 출력합니다.', max_length=255)),
                ('peopleNmEn', models.CharField(blank=True, help_text='스텝명(영문)을 출력합니다.', max_length=255, null=True)),
                ('staffRoleNm', models.CharField(help_text='스텝역할명을 출력합니다.', max_length=255)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs_details', to='kobis.movie')),
            ],
        ),
    ]
