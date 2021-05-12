# adoption/models.py
from djongo import models


class Url(models.Model):
    url = models.CharField(max_length=100)
    _id = models.ObjectIdField()
    def __str__(self):
        return f'{self.url} {self._id}'
