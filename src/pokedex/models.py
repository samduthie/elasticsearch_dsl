from django.contrib.auth import get_user_model
from django.contrib import admin
from django.db import models

class Pokemon(models.Model):
    poke_name = models.TextField()
    type = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


admin.site.register(Pokemon)