from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from accounts.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from accounts.forms import RegisterForm
from django.contrib.auth.models import User
from paltar.models import Product


#REGISTER
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Qeydiyyatınız uğurla tamamlanmışdır.")
            return redirect('login')
            
    else:
        form=RegisterForm
            
    return render(request,'register.html',{'form':form})





#LOGIN
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                        password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')

                else:
                    messages.info(request, 'Disabled Account')

            else:
                messages.info(request, 'Check Your Username and Password')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})


#logout
def user_logout(request):
     logout(request)
     return redirect('login')
     

@login_required(login_url='login')
def user_dashboard(request):
    current_user=request.user
    products=current_user.product_client.all()

    context={"products":products}
    return render(request,"dashboard.html",context)



def buy_products(request):
    product= Product.objects.get(id=request.POST['product_id'])
    user= User.objects.get(id=request.POST['user_id'])
    product.client.add(user)
    return redirect('dashboard')


def delete_products(request):
    product= Product.objects.get(id=request.POST['product_id'])
    user= User.objects.get(id=request.POST['user_id'])
    product.client.remove(user)
    return redirect('dashboard')




# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username,
#                                         password=password)

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('index')

#                 else:
#                     messages.info(request, 'Disabled Account')

#             else:
#                 messages.info(request, 'Check Your Username and Password')

#     else:
#         form = LoginForm()

#     return render(request, 'login.html', {'form':form})








# @login_required(login_url="login")












