from django.shortcuts import render
from datetime import  date, datetime
from myapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request,'index.html')

def contact(request):
  if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name = name, email = email ,subject = subject ,message = message ,date=datetime.today())
        contact.save()
        messages.success(request, 'Your messsage has been sent.')
  return render(request,'contact.html')  