# Generated by Django 2.2.4 on 2020-03-17 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200317_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='example',
        ),
        migrations.RemoveField(
            model_name='word',
            name='second_ex',
        ),
        migrations.RemoveField(
            model_name='word',
            name='synonym',
        ),
        migrations.RemoveField(
            model_name='word',
            name='third_definition',
        ),
        migrations.RemoveField(
            model_name='word',
            name='third_ex',
        ),
        migrations.AlterField(
            model_name='word',
            name='definition',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='word',
            name='second_definition',
            field=models.TextField(blank=True),
        ),
    ]