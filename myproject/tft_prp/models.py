from django.db import models

# Create your models here.

# when adding new model:
#   python manage.py makemigration
#   python manage.py migrate

class Output(models.Model):
    level = models.IntegerField()
    unit_cost = models.IntegerField()
    hits = models.IntegerField()
    times_to_roll = models.IntegerField()

