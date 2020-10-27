# Generated by Django 3.1.2 on 2020-10-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idLibro', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('titulo', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=100)),
                ('numPags', models.IntegerField()),
            ],
        ),
    ]
