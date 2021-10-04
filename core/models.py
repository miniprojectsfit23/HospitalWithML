from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator
import uuid
# Create your models here.


class User(AbstractUser):
    isDoctor = models.BooleanField(verbose_name="Is User a Doctor?")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_pic=models.ImageField(verbose_name="Profile Photo",upload_to="core/static/core/images/profile_pics/",default=None,null=True,blank=True)
    first_name = models.CharField(max_length=200, verbose_name="First Name")
    last_name = models.CharField(max_length=200, verbose_name="Last Name")
    username = models.EmailField(
        max_length=254, unique=True, verbose_name="Email")
    password = models.CharField(max_length=500, verbose_name="Password")
    slug = models.SlugField(max_length=100, unique=True)
    activated = models.BooleanField(
        default=False, verbose_name="Is User activated?")
    # for patients
    age = models.PositiveIntegerField(
        validators=[MaxValueValidator(200)], verbose_name="Age", default=None)
    disease = models.CharField(
        max_length=200, verbose_name="Diseases", default=None)
    allergies = models.CharField(
        max_length=200, verbose_name="Allergies", default=None)
    # for doctors
    specialization = models.CharField(
        max_length=200, verbose_name="Specialization of Doctor", default=None)
    patients = models.ManyToManyField(
        "self", verbose_name="Patients Doctor is Treating", symmetrical=False, blank=True)

    def __str__(self):
        return(self.first_name+" "+self.last_name)

    def get_full_name(self):
        return(self.first_name+" "+self.last_name)

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name+self.last_name)
        super().save()


class Doctor(User):
    class Meta:
        proxy = True


class Patient(User):
    class Meta:
        proxy = True
