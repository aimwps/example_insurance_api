# Generated by Django 4.0.4 on 2022-05-05 15:22

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('document', models.FileField(upload_to='uploads/documents/', validators=[django.core.validators.FileExtensionValidator(['csv'])])),
                ('has_been_converted', models.BooleanField(default=False)),
            ],
        ),
    ]
