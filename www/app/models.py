from django.db import models

from os import path


class SomeFile(models.Model):
    file = models.FileField("Some file")

    def basename(self):
        return path.basename(self.file.name)

