# Generated by Django 3.0.3 on 2020-02-19 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='winRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winRate', models.DecimalField(decimal_places=3, max_digits=3)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Agent')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Game'),
        ),
    ]
