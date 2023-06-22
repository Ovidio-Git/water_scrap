# Generated by Django 4.0 on 2023-06-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reto1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencias',
            name='caratula',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='link_sentencia',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='nombre_proyecto',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='relacionada',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='rol',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='tipo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='tribunal',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='url_sentencia',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='valoresjudisprudencias',
            name='item',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='valoresjudisprudencias',
            name='parametro',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='valoresjudisprudencias',
            name='valor',
            field=models.CharField(max_length=400, null=True),
        ),
    ]