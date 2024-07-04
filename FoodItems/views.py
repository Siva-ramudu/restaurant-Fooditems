from django.shortcuts import render,redirect
from . models import Fooditems,Staff
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request,'home.html')
@login_required(login_url='signin')
def addItem(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        foodtype = request.POST.get('foodtype')
        image = request.FILES.get('image')
        Recipe = request.FILES.get('Recipe')
        
        Fooditems.objects.create(
            name=name,
            price=price,
            foodtype=foodtype,
            image=image,    
            Recipe=Recipe
        )
    return render(request,"Fooditems/addItem.html")

def menu(request):
    menu=Fooditems.objects.all()
    return render(request,"Fooditems/menu.html",{'menu':menu})

def deleteItem(request,id):
    Fooditems.objects.get(id = id).delete()
    return redirect('menu')

def editItem(request,id):
    item = Fooditems.objects.get(id = id)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        foodtype = request.POST.get('foodtype')
        item.name = name
        item.price = price
        item.foodtype = foodtype
        item.save()
        return redirect('menu')
    return render(request,"Fooditems/editItem.html",{'item':item})

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        gender = request.POST.get('name')
        dob = request.POST.get('dob')
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        #checking the existing users to check the username
        usercheck = User.objects.filter(username=username)
        if len(usercheck) > 0 :
            return redirect('signup')

        if password == confirmpassword :
            user=User.objects.create_user(
                username = username,
                password = password
            )

            Staff.objects.create(
                name = name,
                mobile = mobile,
                email = email ,
                gender = gender,
                dob = dob,
                uid_id = user.id
            )
    return render(request,"Fooditems/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = authenticate(username=username, password=password)
        if data is not None :
            login(request,data)
            return redirect('addmenuitem')
    return render(request,'Fooditems/signin.html')
        
def signout(request):
    logout(request)
    # print(request.username)
    return redirect('signin')