from django.contrib.auth import get_user_model
from django.contrib import admin
from django.db import models

class Pokemon(models.Model):
    name = models.TextField()
    type = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


admin.site.register(Pokemon)