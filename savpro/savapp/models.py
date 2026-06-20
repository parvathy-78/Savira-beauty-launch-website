from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


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

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()

        if (
            self.appointment_date and
            self.appointment_date < timezone.localdate()
        ):
            raise ValidationError({
                'appointment_date': 'Past dates are not allowed.'
            })

    def save(self, *args, **kwargs):
        self.full_clean()  # validation force cheyyum
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



