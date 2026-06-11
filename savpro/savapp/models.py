from django.db import models

# Create your models here.
# savapp/models.py

from django.db import models

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('Bridal Makeup', 'Bridal Makeup'),
        ('Hair Styling', 'Hair Styling'),
        ('Hair Spa', 'Hair Spa'),
        ('Facial Treatment', 'Facial Treatment'),
        ('Nail Art', 'Nail Art'),
        ('Skin Care', 'Skin Care'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    # Dropdown field
    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    appointment_date = models.DateField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



