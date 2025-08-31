from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages

# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage(/)")
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Portfolio Contact from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            email_message = EmailMessage(
                subject,
                body,
                email,  # sender (user's email)
                ["noorlal2004@gmail.com"],  # your email
            )
            email_message.reply_to = [email]
            email_message.send()

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")
            return redirect("contact")

    return render(request, "contact.html")
def project(request):
    return render(request, 'project.html')
