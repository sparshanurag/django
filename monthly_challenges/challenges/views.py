
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response 
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "febuary": "Walk for 20 minutes daily",
    "march": "Learn Django 20 minutes a day",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for 20 minutes daily",
    "june": "Learn Django 20 minutes a day",
    "july": "Eat no meat for the entire month!",
    "august":"Walk for 20 minutes daily",
    "september": "Learn Django 20 minutes a day",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for 20 minutes daily",    "december": "Learn Django 20 minutes a day"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</li>"
    
    #"<li><a href="...">January</a></li><li><a href="...">Febuary</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month -1 ]
    redirect_path = reverse("month-challenge", args=[redirect_month ]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
         challenge_text = monthly_challenges[month]
         response_data = f"<h1>{challenge_text}</h1>"
         return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
     
    
        