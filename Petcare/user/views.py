from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template import loader
from .models import QuickEnquiry, Newsletter, Contacts, DogAdopt,Donation
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

def Index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def Adopt(request):
    return render(request, 'adopt.html')


def Service(request):
    return render(request, 'service.html')


def Contact(request):
    return render(request, 'contact.html')


def About(request):
    return render(request, 'about.html')


def Gallary(request):
    return render(request, 'gallary.html')


def Services(request):
    return render(request, 'services.html')

def donate(request):
    return render (request,'donate.html')


def saveEnquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        location = request.POST.get('location')
        message = request.POST.get('message')
        service = request.POST.get('service')

        en = QuickEnquiry(name=name, email=email, mobile=mobile, location=location, message=message, service=service)
        en.save()
        messages.success(request, 'Your request send successfully .')

        # return HttpResponse("Enquiry saved successfully!")  # Return an HttpResponse after saving the enquiry
    return render(request, 'index.html')


def newsLetter(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        ne = Newsletter(name=name, email=email)
        ne.save()
        messages.success(request,' Thank you for Subscription!. ' )
        send_mail(
            subject='Thank You for Subscribing!',
            message=f'Hello dear {name} ,Thank you for subscribing to our newsletter. Get ready to receive heartwarming rescue stories, important updates, and exclusive content. Together, we all make a pawsitive impact on street animals',
            from_email='streetpawcare.info@gmail.com',
            recipient_list=[email],
            fail_silently=True,
        )
    return render(request, 'index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            subject='Thank You for contacts!',
            message=f'Hello dear {name} ,Thank you for subscribing to our newsletter./n Get ready to receive heartwarming rescue stories, important updates, and exclusive content. /n  Together, we all make a pawsitive impact on street animals',
            from_email='streetpawcare.info@gmail.com',
            recipient_list=[email],
            fail_silently=True,
        )

        # Create a Contact object and save it
        cont = Contacts(name=name, email=email, subjects=subject, messages=message)
        cont.save()
        messages.success(request, ' Request send Successfully! ')

        # Optionally, you can redirect to a success page or return a response
        # return redirect('success-page')
    return render(request, 'contact.html')


def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            # messages.error(request, 'An error occurred.')
            return render(request, 'login.html')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.success(request, ' Your password is not same .')
             

        else:

            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            subject = 'Congrats !'
            message = 'Your registration is Successfull'
            email_from = "streetpawcare.info@gmail.com"
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            # message.success(request, "Success")
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            # messages.success(request, "u r loged in")
            return redirect('index')
        else:
            #  messages.success(request, "Username or Password is incorrect!!!")
            return render(request, 'login.html')
    else:
            #  messages.success(request, "Username or Password is incorrect!!!")
            return render(request, 'login.html')
        


def LogoutPage(request):
    logout(request)
    return redirect('index')


def adoptform(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        dogname = request.POST.get('dogname')     

        adop = DogAdopt(fullname=fullname, contact=contact, email=email, address=address, dogname=dogname,
                        )
        adop.save()
        messages.success(request,'Your adoption request has been saved. ' )
        return redirect('adopt')

    return render(request, 'adoptform.html')


def donate(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        donation_amount = request.POST.get('donation_amount')
        payment_method = request.POST.get('payment_method')

        don = Donation(full_name=full_name,email=email,donation_amount=donation_amount,payment_method=payment_method)
        don.save()
        messages.success(request,'Your donation request has been saved. ' )
        return redirect('about')

    return render(request, 'donate.html') 
