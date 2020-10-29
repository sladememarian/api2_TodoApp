from django.db import models

# TODO Add category
# TODO Add logo
# TODO Add user
# TODO Add priority
# TODO Add color
# TODO Add should_notify?
# TODO Add Recurrency
# TODO Add Score
# TODO Add due_date
# TODO Add description


class Task(models.Model):
    name = models.CharField(max_length=50)
    register_date = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
