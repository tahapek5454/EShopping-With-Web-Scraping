from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
def login_request(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    
    if request.method == "POST":
        kullanici_adi=request.POST["username"]
        parola=request.POST["password"]
        
        user=authenticate(request,username=kullanici_adi,password=parola)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"authentication/login.html",{
                "error": "Kullanıcı adı veya şifre yanlış."
            })
            
    return render(request,"authentication/login.html")

def register_request(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    
    if(request.method=="POST"):
        username=request.POST["username"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]
        phonenumber=request.POST["phone"]
        isim=request.POST["firstname"]
        soyisim=request.POST["lastname"]
        email=request.POST["email"]
        adres=request.POST["adres"]
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"authentication/register.html",{
                "error": "Böyle bir kullanıcı zaten var.",
                "username": username,
                "email": email,
                "firstname": isim,
                "lastname": soyisim,
                "phonenumber": phonenumber,
                "adres":adres
            })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"authentication/register.html",{
                    "error": "Girilen email zaten kullanılıyor.",
                     "username": username,
                     "email": email,
                     "firstname": isim,
                     "lastname": soyisim,
                     "phonenumber": phonenumber,
                     "adres":adres
                })
                else:
                    user= User.objects.create_user(username=username,email=email,first_name=isim,last_name=soyisim,password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request,"authentication/register.html",{
                "error": "Girilen parolalar eşleşmiyor.",
                 "username": username,
                 "email": email,
                 "firstname": isim,
                 "lastname": soyisim,
                 "phonenumber": phonenumber,
                 "adres":adres
            })
    

    return render(request,"authentication/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")
