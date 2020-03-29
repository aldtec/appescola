# Generated by Django 3.0.4 on 2020-03-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
                ('data', models.DateField()),
                ('observ', models.CharField(choices=[('F', 'FERIADO'), ('R', 'RECESSO'), ('P', 'PONTO FACULTATIVO'), ('L', 'DIA NÃO LETIVO')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('rf_vinc', models.CharField(max_length=12)),
                ('qpe', models.CharField(blank=True, max_length=4)),
                ('cargo', models.CharField(blank=True, default='Professor Educ. Infantil e Ens. Fund. I', max_length=50)),
                ('regencia', models.CharField(blank=True, max_length=20)),
                ('hor_col', models.CharField(blank=True, max_length=30)),
                ('turma', models.CharField(blank=True, max_length=6)),
                ('horario', models.CharField(blank=True, max_length=80)),
                ('jornada', models.CharField(choices=[('J', 'JEIF'), ('D', 'JBD'), ('B', 'JB')], default='D', max_length=1)),
            ],
        ),
    ]
