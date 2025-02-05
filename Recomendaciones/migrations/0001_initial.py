# Generated by Django 3.0.6 on 2020-07-19 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Logauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomendacion', models.TextField(blank=True)),
                ('fecha_recomendacion', models.DateTimeField()),
                ('tipo_recomendacion', models.CharField(choices=[('25', '25%'), ('50', '50%'), ('75', '75%')], max_length=2)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Logauth.Profile')),
            ],
        ),
    ]
