from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponse
from admin_post.models import Books
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def Logout(request):
    logout(request)
    return redirect('book_site:login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('admin_post:books')
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password2'])
            user.save()
            return redirect('book_site:login')
        else:
            return HttpResponse('نام کاربر یا ایمیل اشتباه است')

    else:
        form = UserSignupForm()
    context = {'form': form}
    return render(request, 'book_site/sign up.html', context)


def Login_user(request):
    if request.user.is_authenticated:
        return redirect('admin_post:books')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(request, email=User.objects.get(username=email), password=password)

        except:
            user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("admin_post:books")
        else:
            HttpResponse('فیلد ها پرنشده')
            return render(request, "book_site/login.html")
    else:
        return render(request, 'book_site/login.html', {})


@login_required(login_url='/book_site/login/')
def profileUser(request, user_id):
    print(user_id)
    profile = Profile.objects.get(user_id=user_id)
    context = {
        'profile': profile
    }
    return render(request, 'book_site/profile.html', context)


@login_required(login_url='/book_site/login/')
def shopingView(request, id):
    url = request.META.get('HTTP_REFERER')
    book = get_object_or_404(Books, id=id)

    if book.user.filter(id=request.user.id).exists():
        book.user.remove(request.user)

    else:
        book.user.add(request.user)

    return redirect(url)


@login_required(login_url='/book_site/login/')
def shopingCart(request):
    users = request.user.shop_book.all()
    context = {
        "book": users,
    }
    return render(request, 'book_site/shopiing-cart.html', context)

