# Generated by Django 4.2.4 on 2023-08-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('charge', models.IntegerField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
    ]