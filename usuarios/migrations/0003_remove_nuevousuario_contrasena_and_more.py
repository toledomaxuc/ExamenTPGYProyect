# Generated by Django 4.1.2 on 2023-07-05 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nuevousuario',
            name='contrasena',
        ),
        migrations.AddField(
            model_name='nuevousuario',
            name='password1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='nuevousuario',
            name='password2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='nuevousuario',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='nuevousuario',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]
