from datetime import datetime, timezone

from django.db import models

# Create your models here.
from users.models import User


class Vocable(models.Model):
    vocab = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.vocab} ({self.translation})"


class StudiedVocable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vocab = models.ForeignKey(Vocable, on_delete=models.CASCADE)
    last_studied = models.DateTimeField(blank=True)
    correct_studied = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'vocab')

    def __str__(self):
        if self.last_studied is not None:
            timediff = (datetime.now(timezone.utc) - self.last_studied)
            if timediff.days >= 1:
                return f"{self.vocab.vocab} ({timediff.days} days ago)"
            else:
                return f"{self.vocab.vocab} ({timediff.total_seconds()/3600:.1f} hours ago)"
        return f"{self.vocab.vocab} (unstudied)"


class Set(models.Model):
    name = models.CharField(max_length=200)
    vocabs = models.ManyToManyField(Vocable, related_name='sets', blank=True)

    def __str__(self):
        return self.name
