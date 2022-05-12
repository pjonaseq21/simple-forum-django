from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib import messages

def sendMail(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an email with Django"
            message = cd['message']

            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            # set the variable initially created to True
            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'login.html', {

        'form': form,
        'messageSent': messageSent,

    })

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        passwd = request.POST['password']

        user = auth.authenticate(username=email, password=passwd)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Credientials invalid")
            return redirect('/login')
    else:
        return render(request, 'login.html')


    
    



