from django.db import models
from django.utils import timezone


class CalculateResults(models.Model):
    result_num = models.IntegerField()
    date_result = models.DateTimeField(
        default=timezone.now
    )
    username = models.CharField(max_length=30)
    input_a = models.IntegerField()
    input_b = models.IntegerField()
    input_c = models.IntegerField()
