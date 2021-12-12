from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# from cryptography.fernet import Fernet
import hashlib


EMAIL_HOST_USER = 'sw33tpeace100@gmail.com'
# Create your views here.
def index(request):
    return render(request,'index.html')


# def genwriekey():
#     key = Fernet.generate_key()
#     with open("pass.key", "wb") as key_file:
#         key_file.write(key)

# def call_key():
#     return open("pass.key", "rb").read()

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

def LoginView(request):
    return render(request,'registration/login.html')

def LogoutView(request):
    return render(request,'logout.html')

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm() 

    return render(request,'registration/register.html',{'form':form})


def sendMail(request):
    message = request.POST.get('message','')

    hash_object = hashlib.sha256(message.encode())
    # hash_message = hashlib.sha256(message.decode())

    subject = request.POST.get('subject','')
    email_id = request.POST.get('email','')
    email = send_mail(subject,hash_object.hexdigest(),EMAIL_HOST_USER,[email_id])


    # file = request.FILES['file']
    # email.attach(file.name, file.read(), file.content_type)

    # uploaded_file = request.FILES['file']
    # email.attach(uploaded_file.namee, uploaded_file.read(), uploaded_file.content_type)
    
    # email.content_subtype='html'
    # email.send()
    return HttpResponse("your mail has been sent successfully!")
    return render(request, 'celebration.html')

# def sendMail(request):
#     send_mail('Hello from SFUAC',
#     'hello there. This is an automated message',
#     'sw33tpeace100@gmail.com',
#     ['yeciy64787@hypteo.com'],
#     fail_silently=False)

#     return render(request,'dashboard.html')