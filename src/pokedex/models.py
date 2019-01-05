from django.contrib.auth import get_user_model
from django.contrib import admin
from django.db import models

class Pokemon(models.Model):
    name = models.TextField()
    type1 = models.TextField()
    type2 = models.TextField()

    total_stats = models.IntegerField()
    generation = models.IntegerField()

    is_legendary = models.BooleanField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id', 'total_stats']


admin.site.register(Pokemon)
