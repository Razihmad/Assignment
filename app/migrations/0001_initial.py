# Generated by Django 2.2.19 on 2021-05-16 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNumber', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=200)),
                ('Maths', models.IntegerField()),
                ('Physics', models.IntegerField()),
                ('Chemistry', models.IntegerField()),
                ('Total', models.IntegerField()),
                ('Percentage', models.IntegerField()),
            ],
        ),
    ]