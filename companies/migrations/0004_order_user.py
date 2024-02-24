# Generated by Django 4.2.5 on 2024-02-24 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0003_service_company_phone_day_of_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.order')),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order_user',
            },
        ),
    ]