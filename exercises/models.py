from django.db import models
from vocabulary.models import StudiedVocable

# Create your models here.


class Sentence(models.Model):
    vocab = models.ForeignKey(StudiedVocable, on_delete=models.CASCADE)
    sentence = models.CharField(max_length=500)

    def __str__(self):
        return f"({self.vocab.vocab}) {self.sentence[:50]}{'...' if len(self.sentence) > 50 else ''}"


class Correction(models.Model):
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    note = models.CharField(max_length=500)

    def __str__(self):
        return self.note[:50]
