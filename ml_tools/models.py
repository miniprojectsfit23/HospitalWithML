from django.db import models
import uuid


# Create your models here.
class MalariaImage(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	image=models.ImageField(verbose_name="Malaria Image",upload_to="ml_tools/static/ml_tools/images/malaria_uploads/",default=None,null=True)
class PneumoniaImage(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	image=models.ImageField(verbose_name="Pneumonia Image",upload_to="ml_tools/static/ml_tools/images/pneumonia_uploads/",default=None,null=True)