# Generated by Django 3.2.12 on 2023-10-12 10:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('color_code', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('color', models.ManyToManyField(to='app1.Colors')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='youtube')),
            ],
        ),
        migrations.CreateModel(
            name='PeopleAddress',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField()),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='app1.people')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
