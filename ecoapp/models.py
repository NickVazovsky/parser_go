from django.db import models


# Create your models here.

class SaveUrl(models.Model):
    url = models.CharField(max_length=1000)


class Questions(models.Model):
    title = models.CharField(max_length=512)
    identifier = models.CharField(max_length=256)
    url = models.CharField(max_length=1024)

    def __str__(self):
        return "{} - {}".format(self.identifier, self.title)


class Prov(models.Model):
    title = models.CharField(max_length=255)


class Results(models.Model):
    base_url = models.CharField(default=True, max_length=255)
    url = models.CharField(default=True, max_length=255)
    title = models.CharField(default=True, max_length=255)
    description = models.CharField(default=True, max_length=255)
    title_unique = models.CharField(default=True, max_length=255)
    description_unique = models.CharField(default=True, max_length=255)
    keywords = models.CharField(default=True, max_length=255)
    yandex = models.CharField(default=True, max_length=255)
    google = models.CharField(default=True, max_length=255)
    h1 = models.CharField(default=True, max_length=255)
    h2 = models.CharField(default=True, max_length=255)
    vk = models.CharField(default=True, max_length=255)
    facebook = models.CharField(default=True, max_length=255)
    instagram = models.CharField(default=True, max_length=255)
    broken_link = models.CharField(default=True, max_length=255)

