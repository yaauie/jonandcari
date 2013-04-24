from django.db import models
import re

BOOLEAN_CHOICES = ((True, 'Yes'), (False, 'No'))


class Rsvp(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_attending = models.NullBooleanField(choices=BOOLEAN_CHOICES, null=True)
    attendees = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    key = models.CharField(max_length=32, unique=False)
    count = models.IntegerField(default=1, null=True)

    def plus_one_situation(self):
        return self.count - 1

    def get_attendees(self):
        return re.split("(?:\\r)?\\n", self.attendees.strip())

    def __unicode__(self):
        return self.attendees.replace("\\n", ", ").rstrip(", ")
