from django.db import models

class WinningRecord(models.Model):
    numbers = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Winning Record {self.id}"
