# Generated by Django 3.0.6 on 2020-07-20 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recomendaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendacion',
            name='tipo_recomendacion',
            field=models.CharField(choices=[('25', '25%'), ('50', '50%'), ('75', '75%'), ('100%', '100%')], max_length=4),
        ),
    ]
