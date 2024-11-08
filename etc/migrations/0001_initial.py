# Generated by Django 4.2.5 on 2024-04-05 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('rank', models.IntegerField(null=True)),
                ('type_of_ownership', models.CharField(max_length=150, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Day_of_work',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('time_open', models.TimeField()),
                ('time_close', models.TimeField()),
                ('day_of_start_week', models.DateField()),
                ('weekday', models.IntegerField()),
            ],
            options={
                'db_table': 'day_of_work',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'holiday',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_role',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'specialization',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('roles', models.ManyToManyField(to='etc.role')),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etc.specialization')),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etc.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etc.user')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=15)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etc.company')),
            ],
            options={
                'db_table': 'phone',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etc.company')),
                ('services', models.ManyToManyField(to='etc.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etc.user')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='day_of_work',
            field=models.ManyToManyField(to='etc.day_of_work'),
        ),
        migrations.AddField(
            model_name='company',
            name='holidays',
            field=models.ManyToManyField(to='etc.holiday'),
        ),
        migrations.AddField(
            model_name='company',
            name='services',
            field=models.ManyToManyField(to='etc.service'),
        ),
        migrations.AddField(
            model_name='company',
            name='specializations',
            field=models.ManyToManyField(to='etc.specialization'),
        ),
    ]
