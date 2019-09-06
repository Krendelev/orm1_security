from datetime import datetime
from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        departure = self.leaved_at or timezone.now()
        return departure - self.entered_at

    def get_formatted_duration(self):
        duration = self.get_duration()
        return "{num[0]}:{num[1]}".format(num=str(duration).split(":"))

    def is_long(self, minutes=60):
        return self.get_duration().total_seconds() > minutes * 60

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at)
            if self.leaved_at
            else "not leaved",
        )
