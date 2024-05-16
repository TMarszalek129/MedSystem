from django.db import models

class Patient(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthdate = models.DateField(null=True)
    login = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"