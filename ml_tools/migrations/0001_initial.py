# Generated by Django 3.0.5 on 2021-10-04 06:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MalariaImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(default=None, null=True, upload_to='ml_tools/static/ml_tools/images/malaria_uploads/', verbose_name='Malaria Image')),
            ],
        ),
        migrations.CreateModel(
            name='PneumoniaImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(default=None, null=True, upload_to='ml_tools/static/ml_tools/images/pneumonia_uploads/', verbose_name='Pneumonia Image')),
            ],
        ),
    ]