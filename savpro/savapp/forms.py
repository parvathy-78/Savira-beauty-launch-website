from django import forms
from .models import Booking
from django.utils import timezone


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': timezone.localdate().strftime('%Y-%m-%d')
                }
            ),
            'appointment_time': forms.TimeInput(
                attrs={'type': 'time'}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        appointment_date = cleaned_data.get('appointment_date')
        appointment_time = cleaned_data.get('appointment_time')

        # Past date validation
        if appointment_date and appointment_date < timezone.localdate():
            raise forms.ValidationError(
                "Past dates are not allowed."
            )

        # If selected date is today, prevent past times
        if (
            appointment_date == timezone.localdate()
            and appointment_time
        ):
            current_time = timezone.localtime().replace(
                second=0,
                microsecond=0
            ).time()

            if appointment_time < current_time:
                raise forms.ValidationError(
                    "Past time is not allowed for today."
                )

        return cleaned_data

