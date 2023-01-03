from django.db import models


class FileDir(models.Model):
    FileDir = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.FileDir

class FileAxis(models.Model):
    XAxis = models.CharField(max_length=25)
    YAxis = models.CharField(max_length=25)

    def __str__(self) -> str:
        return '{} {}'.format(self.XAxis,self.YAxis)
