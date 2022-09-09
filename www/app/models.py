from django.db import models
from django.urls import reverse

from os import path


class FileField(models.FileField):
    @property
    def url(self):
        return reverse("media", kwargs={"pk": self.instance.pk})


class SomeFile(models.Model):
    file = FileField("Some file")

    def basename(self):
        return path.basename(self.file.name)

