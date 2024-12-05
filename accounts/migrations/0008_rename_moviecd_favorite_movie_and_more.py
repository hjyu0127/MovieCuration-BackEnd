# Generated by Django 5.1.3 on 2024-12-05 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_movie_id_favorite_moviecd_and_more'),
        ('kobis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='movieCd',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='id',
            new_name='movieCd',
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'movie')},
        ),
    ]
