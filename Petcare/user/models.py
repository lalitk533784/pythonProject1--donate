from django.db import models


class QuickEnquiry(models.Model):
   
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=12)
    location = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    SERVICE_CHOICES = (
        ('1', 'High'),
        ('2', 'Medium'),
        ('3', 'Low'),
    )
    service = models.CharField(max_length=1, choices=SERVICE_CHOICES, default='1')


class Newsletter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    

class Contacts(models.Model):
    name =models.CharField(max_length=255)
    email =models.EmailField()
    subjects =models.CharField(max_length=255)
    messages = models.TextField()
   

class DogAdopt(models.Model):
    fullname = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)  # Assuming the contact number can be stored as a string
    email = models.EmailField()
    address = models.TextField()
    # dogname = models.CharField(max_length=255, choices=[
    #     ("Sheru", "Sheru"),
    #     ("Moti", "Moti"),
    #     ("Tiger", "Tiger"),
    #     ("Lucy", "Lucy"),
    #     ("Danny", "Danny"),
    #     ("Marco", "Marco"),
    # ])
    DOGNAME_CHOICES = (
        ("Sheru", "Sheru"),
        ("Moti", "Moti"),
        ("Tiger", "Tiger"),
        ("Lucy", "Lucy"),
        ("Danny", "Danny"),
        ("Marco", "Marco"),
    )
    dogname = models.CharField(max_length=10, choices=DOGNAME_CHOICES, default='1')
    




class Donation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
        ('bankTransfer', 'Bank Transfer'),
    ])
    timestamp = models.DateTimeField(auto_now_add=True)

    





