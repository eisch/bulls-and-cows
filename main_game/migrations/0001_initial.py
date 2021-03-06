# Generated by Django 2.0.6 on 2018-10-25 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('bull', models.IntegerField()),
                ('cow', models.IntegerField()),
                ('last_entered_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('current_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_game.CurrentResult')),
            ],
        ),
    ]
