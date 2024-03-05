from django.db import models

# Create your models here.

class Doctor(models.model):
    name = models.charfield(max_length=50)
    mobile = models.integerfield()
    special = models.charfield(max_length=50)

def __str__(self):
        return self.name

class patient(models.model):
    name=models.charfield(max_length=50)
    gender=models.charfield(max_length=50)
    mobile=models.intigerfield(null=True)
    address=models.charfield(max_length=100)

def __str__(self):
        return self.name

class Appointment(models.model):
    Doctor=models.foreignkey(Doctor,on_delete=models.CASCADE)
    Patient = models.foreignkey(patient, on_delete=models.CASCADE)
    Date1=models.DateField()
    Time1=models.timefield()


def __str__(self):
        return self.doctor.name+"__"+self.patient.name
