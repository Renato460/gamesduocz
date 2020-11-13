from django.shortcuts import render, redirect
from .forms import ContactForms
from django.core.mail import EmailMessage
from django.urls import reverse
# Create your views here.


def contacto(request):
    formulario = ContactForms()
    if request.method == 'POST':
        formulario = ContactForms(data=request.POST)
        if formulario.is_valid:
            nombre= request.POST.get('nombre','')
            correo = request.POST.get('correo','')
            mensaje = request.POST.get('mensaje','')
            email = EmailMessage('Le han contactado',
            '{} {}: dijo {}'.format(nombre,correo,mensaje),
            'pruebatest354@gmail.com',['pruebatest354@gmail.com'],
            reply_to=[correo])
            try:
                email.send()
                return redirect(reverse('contacto'))
            except Exception as e:
                return redirect(reverse('contacto'))
    return render(request,'contacto.html',{'form':formulario})