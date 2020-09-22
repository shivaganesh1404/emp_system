from django.db import models


class File(models.Model):
    mobile_number = models.CharField(max_length=50)
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
