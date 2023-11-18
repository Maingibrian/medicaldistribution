from django.db import models
from django.contrib.auth.models import User

class institution(models.Model):
    LOCATION_CHOICES = [
        ('Nakuru', 'Nakuru'),
        ('Mombasa', 'Mombasa'),

    ]
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)

    institution_ID = models.IntegerField( )
    name = models.CharField(null=True,  max_length=255)
    location = models.CharField(null=True, max_length=255, choices=LOCATION_CHOICES)

    def __str__(self):
        return (f"{self.name}  " )

class County_Health_Worker(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)

    workerID = models.IntegerField( )
    fullName = models.CharField(max_length=255)
    designation = models.CharField(null=True, max_length=255)

    def __str__(self):
        return (f"{self.fullName}")

class medication_package(models.Model):
    STATUS = (
        ("Pending", 'pending'),
        ("Delivered", 'Delivered')
    )
    county_Health_Worker = models.ForeignKey(County_Health_Worker, null=True, on_delete=models.SET_NULL)
    Institution = models.ForeignKey(institution, null=True, on_delete=models.SET_NULL)
    packageID = models.AutoField(primary_key=True, unique=True)
    medicationName = models.CharField(null=True, max_length=255)
    batchNumber = models.CharField(null=True, max_length=255)
    expiryDate = models.DateField()
    quantity = models.IntegerField(null=True)
    status = models.CharField(null=True, max_length=255, choices=STATUS)

    def __str__(self):
        return f"{self.medicationName}"



class MedicationDistribution(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    package = models.ForeignKey(medication_package, on_delete=models.CASCADE)
    institution = models.ForeignKey(institution, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.package.medicationName} to {self.institution.name}"




class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    package = models.ForeignKey(MedicationDistribution, null=True, blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

class auditor(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)

    auditorID = models.IntegerField( )
    auditorName = models.CharField(max_length=255)
    designation = models.CharField(null=True, max_length=255)