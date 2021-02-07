# Generated by Django 3.1.6 on 2021-02-07 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('photo_url', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='methods', to='therapists_profiles.therapist')),
            ],
        ),
    ]
