from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Tudo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    title = models.TextField(max_length=255)
    content = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(auto_now=False)

    def __str__(self):
        return self.content





