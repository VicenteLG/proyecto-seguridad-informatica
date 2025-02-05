# Generated by Django 3.0.6 on 2020-07-19 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Logauth', '0001_initial'),
        ('Recomendaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_control', models.CharField(max_length=100)),
                ('porcentaje_cumplimiento', models.PositiveIntegerField(default=0)),
                ('porcentaje_no_cumplimiento', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Dominio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_dominio', models.CharField(max_length=75)),
                ('porcentaje_cumplimiento', models.PositiveIntegerField(default=0)),
                ('porcentaje_no_cumplimiento', models.PositiveIntegerField(default=0)),
                ('recomendacion', models.ManyToManyField(blank=True, null=True, to='Recomendaciones.Recomendacion')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Logauth.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Logauth.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Subcontrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_subcontrol', models.TextField(blank=True)),
                ('total', models.BooleanField(default=False)),
                ('respuesta', models.ManyToManyField(blank=True, null=True, to='ChartsGAP.Respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_seccion', models.CharField(max_length=75)),
                ('porcentaje_cumplimiento', models.PositiveIntegerField(default=0)),
                ('porcentaje_no_cumplimiento', models.PositiveIntegerField(default=0)),
                ('control', models.ManyToManyField(blank=True, null=True, to='ChartsGAP.Control')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje_cumplimiento', models.PositiveIntegerField(default=0)),
                ('porcentaje_no_cumplimiento', models.PositiveIntegerField(default=0)),
                ('dominio', models.ManyToManyField(blank=True, null=True, to='ChartsGAP.Dominio')),
            ],
        ),
        migrations.AddField(
            model_name='dominio',
            name='seccion',
            field=models.ManyToManyField(blank=True, null=True, to='ChartsGAP.Seccion'),
        ),
        migrations.AddField(
            model_name='control',
            name='subcontrol',
            field=models.ManyToManyField(blank=True, null=True, to='ChartsGAP.Subcontrol'),
        ),
    ]
