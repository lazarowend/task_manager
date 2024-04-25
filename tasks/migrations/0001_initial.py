# Generated by Django 5.0.4 on 2024-04-25 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('priority', models.IntegerField(choices=[(0, 'Alto'), (1, 'Médio'), (2, 'Baixo')])),
                ('status', models.BooleanField()),
                ('limite_date', models.DateField()),
            ],
        ),
    ]