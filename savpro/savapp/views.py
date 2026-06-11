from django.shortcuts import render,redirect


def home(request):
    form = BookingForm()
    return render(request, 'home.html', {'form': form})
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def gallery(request):
    return render(request, 'gallery.html')
def contact(request):
    return render(request, 'contact.html')
def success(request):
    return render(request,'Success.html')
from .forms import BookingForm


from django.shortcuts import render, redirect

def booking(request):
    print("BOOKING VIEW HIT")

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


