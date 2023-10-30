from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Shoe,NewsLetter
from .forms import PaymentForm,SearchForm

def index(request):
   shoes=Shoe.objects.all()
   search=request.GET.get('searchs')
   if request.method=="POST":
      email=request.POST['email']
      reciepient=NewsLetter(email=email)
      reciepient.save()
   if search != None:
      return HttpResponseRedirect(reverse('details',args=[search]))
   
   return render(request,'shoeStore/index.html',{
      "shoes":shoes
   })
def details(request,shoe_name):
   shoe=Shoe.objects.get(name=shoe_name)
   return render(request,'shoeStore/details.html',{
      'shoe':shoe
   })
def payment(request,shoe_name):
   if request.method=="POST":
      payment_form=PaymentForm(request.POST)
      if payment_form.is_valid():
         print(payment_form.cleaned_data)
         payment_form.save()
   payment_form=PaymentForm()
   return render(request,"shoeStore/payment.html",{
      'payment_form':payment_form,
      'shoe_name':shoe_name,
   })