from django.db import models

class Fibonacci(models.Model):
    # this simply maintains the last fibonacci number computed
    last_number = models.PositiveIntegerField(default=0)
