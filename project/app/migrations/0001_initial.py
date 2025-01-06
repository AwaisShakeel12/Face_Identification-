# Generated by Django 5.1 on 2024-11-16 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('selected_classes', models.JSONField(blank=True, null=True)),
                ('result_image', models.ImageField(blank=True, null=True, upload_to='results/')),
            ],
        ),
    ]
