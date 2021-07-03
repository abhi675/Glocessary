from django.shortcuts import render
from .models import Shop,Details,Payment
from django.contrib import messages
# Create your views here.
def index(request):
    shops=Shop.objects.all()
  
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        
        
        if not name or not email or not name.strip() or not email.strip():
            messages.info(request,'Please fill all the informations')
            return render(request,'index.html',{'shops':shops})
          
        elif Details.objects.filter(name=name,email=email).exists():
            messages.info(request,'user is already present, please sign in with your account')
            return render(request,'index.html',{'shops':shops})

        detail=Details(name=name,email=email)
        detail.save()
        messages.info(request,'You are logged in ' + name)
        return render(request,'index2.html',{'name':name})
    
    Email=request.GET.get('Email')
    if Email:
        if Details.objects.filter(email=Email).exists():
            Name=Details.objects.get(email=Email)
            messages.info(request,'congratulations, you have successfully loged in with your email ' + Name.name)
            return render(request,'index.html',{'shops':shops})

        else:
            messages.info(request,'you have signed in with wrong Email, use correct email otherwise subscribe us')
            return render(request,'index.html',{'shops':shops})
    

    
    return render(request,'index.html',{'shops':shops})



def paymentform(request,price,link,productname):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        nameoncard=request.POST.get('nameoncard')
        creditcardnumber=request.POST.get('creditcardnumber')
        date=str(request.POST.get('date'))
        cvv=request.POST.get('cvv')
        Price=request.POST.get('price')
        if not Price or not Price.strip() or int(Price)!=price:
            messages.info(request,'Please fill the correct amount of item')
            return render(request,'index1.html',{'price':price,'link':link,'productname':productname})
        
       
        pay=Payment(name=name,email=email,address=address,nameoncard=nameoncard,creditcardnumber=creditcardnumber,date=date,cvv=cvv,price=price,productname=productname)
        pay.save()
        return render(request,'index3.html',{'name':name})
    return render(request,'index1.html',{'price':price,'link':link,'productname':productname})