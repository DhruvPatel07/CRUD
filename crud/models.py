from django.db import models

# Create your models here.


class Student(models.Model):
    sid = models.CharField(max_length=5)
    sname = models.CharField(max_length=50)
    scontact = models.CharField(max_length=14)

    def _str_(self):
        return self.sname
