# Generated by Django 2.0 on 2017-12-13 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=60)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('type', models.CharField(max_length=30)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timework.Card')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timework.Reader')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='messages',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timework.Worker'),
        ),
        migrations.AddField(
            model_name='card',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timework.Worker'),
        ),
    ]
