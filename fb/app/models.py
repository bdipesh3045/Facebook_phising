from django.db import models


class Data(models.Model):
    username = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.username}:{self.pw}"
