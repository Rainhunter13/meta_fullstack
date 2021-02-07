from django.db import models


# Create your models here.
class Therapist(models.Model):
    airtable_id = models.CharField(max_length=100, default=None)
    name = models.CharField(default=None, null=True, max_length=100)
    photo_url = models.CharField(default=None, null=True, max_length=100)


class Method(models.Model):
    name = models.CharField(max_length=100, default=None)
    therapist = models.ForeignKey(Therapist, related_name='methods', on_delete=models.CASCADE)
