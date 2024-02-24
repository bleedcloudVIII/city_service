# Generated by Django 4.2.5 on 2024-02-24 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_order_user'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='phone',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='phones',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.phone'),
        ),
        migrations.AddField(
            model_name='company',
            name='id_specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.specialization'),
        ),
    ]