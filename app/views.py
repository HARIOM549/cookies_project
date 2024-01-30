from django.shortcuts import render
# Create your views here.
def home(request):

    return render(request,'app/home.html')

def base(request):
    guest="Guest"
    return render(request,'app/base.html',{'guest':guest})

def Signup(request):
    return render(request,'app/Signup.html')

def Login(request):

    return render(request,'app/Login.html')

def about(request):
    return render(request,'app/about.html')


def Contact(request):
    return render(request,'app/Contact.html')
      
def Services(request):
    return render(request,'app/Services.html')

def savedata(request):
    name=request.POST['Name']
    email=request.POST['email']
    contact=request.POST['number']
    city=request.POST['city']
    password=request.POST['password']

    # print(name)
    # print(email)
    # print(contact)
    # print(city)
    # print(password)

    # user='Hello, '+name
    
    response=render(request,'app/Login.html')

    response.set_cookie('Name',name)
    response.set_cookie('email',email)
    response.set_cookie('Contact',contact)
    response.set_cookie('City',city)
    response.set_cookie('Password',password)
    
    return response

def Login_data(request):
    email=request.POST['email']
    pwd=request.POST['password']

    emailid=request.COOKIES['email']
    pswd=request.COOKIES['Password']


    if email==emailid and pwd==pswd:
        name=request.COOKIES['Name']
        return render(request,'app/home.html',{'guest':name})
    
    else:
        msg="Incorrect password or email"
        return render(request,'app/Login.html',{'incoreectmsg':msg})

def delete(request):
    data=render(request,'app/home.html')

    data.delete_cookie('Name')
    data.delete_cookie('email')
    data.delete_cookie('Contact')
    data.delete_cookie('City')
    data.delete_cookie('Password')
    
    return data




    