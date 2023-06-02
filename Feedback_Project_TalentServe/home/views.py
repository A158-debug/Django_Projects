from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Feedback
from django.contrib import  messages

# Create your views here.
def home(request):
    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       desc = request.POST.get('desc')   
       Feedback = Feedback(name=name, email=email, desc=desc, date = datetime.today())
       Feedback.save()
       messages.success(request, "Thank you for your feedback")
       
    return render(request, 'index.html',)
