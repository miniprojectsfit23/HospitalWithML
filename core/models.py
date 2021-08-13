from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator
import uuid
# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200, verbose_name="First Name")
    last_name = models.CharField(max_length=200, verbose_name="Last Name")
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return(self.first_name+" "+self.last_name)

    def get_absolute_url(self):
        return reverse("crud_patients:single", args=[self.slug])
    def save(self, **kwargs):
        if not self.slug:
            self.slug=slugify(self.fname+self.lname)
        super(Patient, self).save()


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    isDoctor = models.BooleanField(default=False, editable=False,verbose_name="Is User a Doctor?")
    age = models.PositiveIntegerField(validators=[MaxValueValidator(200)],verbose_name="Age")
    specialization = models.CharField(max_length=200, verbose_name="Specialization of Doctor")
    disease = models.CharField(max_length=200,verbose_name="Diseases")
    disease = models.CharField(max_length=200,verbose_name="Allergies")


class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    isDoctor = models.BooleanField(default=True, editable=False,verbose_name="Is User a Doctor?")
    specialization = models.CharField(max_length=200, verbose_name="Specialization of Doctor")
    patient = models.ForeignKey(Patient,verbose_name="patientsTreating",on_delete=models.CASCADE)
