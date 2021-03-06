# Generated by Django 3.1.6 on 2021-02-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapists_profiles', '0004_auto_20210208_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyncRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='therapist',
            name='therapist',
            field=models.ManyToManyField(related_name='updated_therapists', to='therapists_profiles.SyncRecord'),
        ),
    ]
