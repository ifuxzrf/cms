from django.db import models


# Create your models here.

class Synonyms(models.Model):
    word = models.CharField(max_length=16, blank=False)
    parent_id = models.IntegerField()
    count = models.IntegerField()
    status = models.SmallIntegerField()
    create_time = models.DateTimeField()


class Emotional(models.Model):
    word = models.CharField(max_length=16, blank=False)
    table_type = models.CharField(max_length=32, blank=False)
    emotion_type = models.CharField(max_length=32, blank=False)
    count = models.IntegerField()
    status = models.SmallIntegerField()
    create_time = models.DateTimeField()


class Sensitive(models.Model):
    word = models.CharField(max_length=16, blank=False)
    table_type = models.CharField(max_length=32, blank=False)
    count = models.IntegerField()
    status = models.SmallIntegerField()
    create_time = models.DateTimeField()

