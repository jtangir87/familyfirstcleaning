from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from .forms import RequestQuoteForm
from django.template.loader import get_template
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, "pages/home.html", {"form": RequestQuoteForm()})


def quoterequest(request):
    if request.method == "POST":

        ## EMAIL CLIENT ##
        template = get_template("pages/quote_request.txt")
        context = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
        }
        content = template.render(context)
        send_mail(
            "New Quote Request",
            content,
            "Website <donotreply@elevatedwebsystems.com>",
            ["info@family1stcleaning.com"],
            fail_silently=False,
        )
    return HttpResponseRedirect(reverse("thank_you"))


def contact_us(request):
    if request.method == "POST":

        ## EMAIL CLIENT ##
        template = get_template("pages/contact_us.txt")
        context = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "subject": request.POST.get("subject"),
            "message": request.POST.get("message"),
        }
        content = template.render(context)
        send_mail(
            "New Contact Form Submitted",
            content,
            "Website <donotreply@elevatedwebsystems.com>",
            ["info@family1stcleaning.com"],
            fail_silently=False,
        )
    return HttpResponseRedirect(reverse("thank_you"))
