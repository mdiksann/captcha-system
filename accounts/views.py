from django.shortcuts import render
from django.contrib import messages
from .forms import MyLoginForm

def login_view(request):
    if request.method == 'POST':
        form = MyLoginForm(request.POST)
        if form.is_valid():
            # Jika captcha benar
            messages.success(request, "Captcha Benar! Anda berhasil login.")
        else:
            # Jika captcha salah
            messages.error(request, "Captcha salah atau data tidak valid. Silakan coba lagi.")
    else:
        form = MyLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})