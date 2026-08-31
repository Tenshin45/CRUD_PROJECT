from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .forms import PasswordChangeForm, ProductForm, UserRegistrationForm, LoginForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
# Create your views here.
def is_admin(user):
    return user.is_staff
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
@login_required
@user_passes_test(is_admin)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redirect to the admin dashboard after successful product creation
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
@login_required
@user_passes_test(is_admin)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                if user.is_staff:
                    return redirect('admin_dashboard')  # Redirect to the admin dashboard if the user is staff
                else:
                    return redirect('user_dashboard')  # Redirect to the user dashboard if the user is not staff
            # Perform login logic here
         #   return redirect('index')  # Redirect to the home page after successful login
    else:
        form = LoginForm()
    #if request.user.is_staff:
     #   return redirect('admin_dashboard')  # Redirect to the admin dashboard if the user is staff
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)  # Log out the user
    #if request.method == 'POST':
        # Perform logout logic here
    return redirect('index')  # Redirect to the home page after logout
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            # Perform password change logic here
            return redirect('index')  # Redirect to the home page after successful password change
    else:
        form = PasswordChangeForm()
    return render(request, 'password_change.html', {'form': form})
@login_required
def product_detail(request, product_id=None):
    if product_id is not None:
        product = get_object_or_404(Product, id=product_id)
    else:
        product = Product.objects.first()  # Get the first product for demonstration purposes
    return render(request, 'view_product.html', {'product': product})
@login_required
@user_passes_test(is_admin)
def product_update(request, product_id=None):
    if product_id is not None:
     product = get_object_or_404(Product, id=product_id)
    else:
     product = None
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redirect to the product detail page after successful update
    else:
        form = ProductForm(instance=product)
    return render(request, 'add_product.html', {'form': form, 'product': product})
@login_required
@user_passes_test(is_admin)
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    #if request.method == 'POST':
    product.delete()
    return redirect('admin_dashboard')  # Redirect to the admin dashboard after successful deletion
    #return render(request, 'product.html', {'product': product})
@login_required
def user_dashboard(request):
    products = Product.objects.all()
    return render(request, 'user_dashboard.html', {'products': products})
def make_payement(request, product_id=None):
   if product_id is not None:
           return HttpResponse("Product not specified", status=400)
           product = get_object_or_404(Product, id=product_id)
   else:
           product = Product.objects.first()  # Get the first product for demonstration purposes
   if request.method=='POST':
        Phone_number=request.POST['number']
        if not Phone_number:
            return HttpResponse("Phone number is required", status=400)
        Amount = product.price
        account_reference="My APP"
        transaction_desc=f"Payement for {product.name}"
        callback_urls="https://crud-project-hfzd.onrender.com/callback/"
        cl=MpesaClient()
        #save payment details in db
        Payment.objects.create(Phone_Number=Phone_number,Amount=Amount,Status="Pending", Merchart_id=response.Merchart_request_id)
        response=cl.stk_push(Phone_number,Amount,account_reference,transaction_desc,callback_urls)
        print(response)
        return HttpResponse('payment initiated')   
   return render(request, 'pay.html',  {'product': product})
@csrf_exempt
def callback(request):
    if request.method=='POST':
        data=request.body
        print("callback data", data)
        return JsonResponse({'status':'success'})
    return JsonResponse({'status':'failure'})