from statistics import mode
from django.db import models


class UserToken(models.Model):
    user_id = models.CharField(max_length=255)
    token = models.TextField()




 