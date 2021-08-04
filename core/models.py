from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    USER_TYPE_CHOICES = (
      (1, 'doctor'),
      (2, 'patient'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return(self.first_name+" "+self.last_name)