from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
    # User is authenticated

# Create your views here.
def home(request):
    liste_voiture=Voiture.objects.all()
    context={"allvoitures":liste_voiture}
    return render(request,"index_2.html",context)
def voiture(request):
    liste_voiture=Voiture.objects.all()
    context={"allvoitures":liste_voiture}
    return render(request,"voiture.html",context)
def about(request):
    return render(request,"about.html")
def contact(request):
     return render(request, 'contact.html')
def detail(request):
    return render(request,"detail.html")
def reservation(request,iden):
     voiture1=Voiture.objects.get(carid=iden)
     if request.method == "POST":
        voiture = Voiture.objects.get(carid=request.POST['voiture'])
        rsvlieuramassage = request.POST['lieuxprise']
        rsvdateramassage = request.POST['dateprise']
        rsvlieuretour = request.POST['lieuxretour']
        rsvdateretour = request.POST['dateretour']
        rsvnomreservant = request.POST['nom']
        rsvprennomreservant = request.POST['prenom']
        rsvmailreservant = request.POST['email']
        rsvphonereservant = request.POST['tel']
        rsvsupinfo = request.POST['information']
        print('id {}'.format(voiture))
        reservation1 = Reservation.objects.create(
            voiture = voiture,
            rsvlieuramassage = rsvlieuramassage,
            rsvdateramassage = rsvdateramassage,
            rsvlieuretour = rsvlieuretour,
            rsvdateretour = rsvdateretour,
            rsvnomreservant = rsvnomreservant,
            rsvprennomreservant = rsvprennomreservant,
            rsvmailreservant = rsvmailreservant,
            rsvphonereservant = rsvphonereservant,
            rsvsupinfo = rsvsupinfo
        )
        reservation1.save()
        messages.success(request, 'FELICITATION RESERVATION REUSSIE.')
     return render(request, 'reservation.html',{"voiture1":voiture1})
     
def login_1(request):
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('account')
            else:
                messages.error(request,'Authentification Echouée')
                return render(request, 'login_1.html',{"form":form})
        else:
        
            return render(request, 'login_1.html',{"form":form})
                
            
        
    else:
        form=LoginForm()
        return render(request, 'login_1.html',{"form":form})



def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            #password2 = form.cleaned_data['password2']
            localisation = form.cleaned_data['localisation']
            user = User.objects.create_user(username=username,password=password,email=email)
            if user is not None:
                
                return redirect("home")
            else:
                messages.error(request,'Creation de compte échouée veillez reesayer')
                return render(request,'register.html',{"form":form})
        else:
            return render(request,'register.html',{"form":form})
        return render(request,'register.html',{})
    form = RegisterForm()
    return render(request, 'register.html',{"form":form})



def logout1(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login_1')
def account(request):
    return render(request, 'account.html')
        
def voiture_details(request,logotype):
    voiture=Voiture.objects.get(carid=logotype)
    return render(request,"voiture_details.html",{"voiture":voiture})