from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse


# Create your views here.

def books(requests):
    context = {
        "book": Books.objects.filter(status="p").order_by("-publish"),
        "book_discount": Books.objects.filter(status="p", discount__isnull=False).order_by("-publish"),
        "category": Category.objects.filter(status=True),
    }
    return render(requests, "book_site/index.html", context)


def bookDetail(requests, slug, id):
    context = {
        "book": get_object_or_404(Books, slug=slug, status="p"),
        "comment_form": comment_form(),
        "comment": comment.objects.filter(book_key_id=id),
    }
    return render(requests, "book_site/post.html", context)


def categorys(requests, slug):
    context = {
        'category': get_object_or_404(Category, slug=slug, status=True),

    }
    return render(requests, "book_site/category.html", context)


def comments(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        comnentt = comment_form(request.POST)
        if comnentt.is_valid():
            data = comnentt.cleaned_data
            comment.objects.create(text=data['text'], user_id=request.user.id, book_key_id=id)

            return redirect(url)
        else:
           return HttpResponse('errors')
    else:
       return redirect(url)

