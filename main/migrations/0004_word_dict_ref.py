# Generated by Django 2.2.4 on 2020-02-22 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191207_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='dict_ref',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Project'),
        ),
    ]
