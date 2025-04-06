from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class GameType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        app_label = 'game_type'

    def __str__(self):
        return self.name

    def clean(self):
        if not self.name:
            raise ValidationError('Name is required')
