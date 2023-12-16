from django.contrib.auth.models import User
from django.db import models
from pytils.translit import slugify


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.EmailField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    slug = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f"{self.name} - {self.title}")
        super().save(force_insert, force_update, using, update_fields)


class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.PositiveIntegerField()
    skills = models.TextField()
    duty = models.TextField()
    email = models.EmailField()
    slug = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = User.objects.get(username='default_username')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name