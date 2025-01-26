from django.shortcuts import render
from .forms import QRForm
import qrcode
import os
from django.conf import settings

def generate_qrCode(request):
    if request.method == 'POST':
        form = QRForm(request.POST)
        if form.is_valid():
            qr_title = form.cleaned_data['qr_title']
            url = form.cleaned_data['url']

            # QR generate
            qr = qrcode.make(url)
            file_name = qr_title.replace(' ', '_').lower() + '.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            # QR Image url
            qr_url = os.path.join(settings.MEDIA_URL, file_name)

            context = {
                'qr_title': qr_title,
                'qr_url': qr_url,
                'file_name': file_name,
            }
            return render(request, 'qr_result.html', context)

    else:
        form = QRForm()
        context = {
            'form': form,
        }
        return render(request, 'generate_qrCode.html', context)