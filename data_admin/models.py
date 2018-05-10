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


class Business_formula(models.Model):
    name = models.CharField(max_length=64, null=False)
    descript = models.CharField(max_length=255, null=False)
    business_id = models.IntegerField()
    keywords = models.CharField(max_length=64, null=False)
    params = models.CharField(max_length=128, null=False)
    formula = models.CharField(max_length=128, null=False)
    status = models.SmallIntegerField()
    table_type = models.SmallIntegerField()

    class Meta:
        index_together = [('name',), ('business_id',)]


class Business_operation(models.Model):
    name = models.CharField(max_length=64, null=False)
    step = models.SmallIntegerField()
    business_id = models.IntegerField()
    keywords = models.CharField(max_length=64, null=False)
    status = models.SmallIntegerField()
    table_type = models.SmallIntegerField()
    create_time = models.DateTimeField(auto_created=True)

    class Meta:
        index_together = [('name',), ('business_id',)]


class Business_production(models.Model):
    product = models.CharField(max_length=64, null=False)
    name = models.CharField(max_length=64, null=False)
    business_id = models.IntegerField()
    description = models.CharField(max_length=255, null=False)
    keywords = models.CharField(max_length=128, null=False)
    status = models.SmallIntegerField()
    table_type = models.SmallIntegerField()
    create_time = models.DateTimeField(auto_created=True)

    class Meta:
        index_together = [('name',), ('business_id',), ('product',)]


class Business_structure(models.Model):
    name = models.CharField(max_length=64, null=False)
    parent_id = models.IntegerField()
    path = models.CharField(max_length=255, null=False)
    bank = models.CharField(max_length=64, null=False)
    area = models.CharField(max_length=64, null=False)
    status = models.SmallIntegerField()
    table_type = models.SmallIntegerField()
    create_time = models.DateTimeField(auto_created=True)

    class Meta:
        index_together = [('name',), ('parent_id',), ('bank',)]
