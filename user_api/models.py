from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    user_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username