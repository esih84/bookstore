from django.shortcuts import render, get_object_or_404
from .models import Books, Category


# Create your views here.

def books(requests):
    context = {
        "book": Books.objects.filter(status="p").order_by("-publish"),
        "book_discount": Books.objects.filter(status="p", discount__isnull=False).order_by("-publish"),
        "category": Category.objects.filter(status=True),
    }
    return render(requests, "book_site/index.html", context)


def bookDetail(requests, slug):
    context = {
        "book": get_object_or_404(Books, slug=slug, status="p"),
    }
    return render(requests, "book_site/post.html", context)


def categorys(requests, slug):
    context = {
        'category': get_object_or_404(Category, slug=slug, status=True),

    }
    return render(requests, "book_site/category.html", context)
