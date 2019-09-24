# Generated by Django 2.2.4 on 2019-09-24 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_word_more_definitions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_id',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_id',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='word',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
