from django.db import models
from django.contrib.auth.models import User
from structure.models import Structure

class UserStructure(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='structure_assignments')
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, related_name='user_assignments')
    assigned_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=50, default='member')

    class Meta:
        unique_together = ('user', 'structure')
        ordering = ['-assigned_at']

    def __str__(self):
        return f"{self.user.username} - {self.structure.name}"
