from django.db import models
from django.utils import timezone
from book_site.models import User
from django.forms import ModelForm
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام')
    photo = models.ImageField(upload_to='images/', verbose_name='عکس')
    description = models.TextField(max_length=1000, verbose_name='توضیحات')
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True,)

    def __str__(self):
        return self.title


class Books(models.Model):
    STATUS_CHOICES = (
        ('p', 'publish'),
        ('n', 'draft'),
    )
    bookName = models.CharField(max_length=500,verbose_name='نام کتاب')
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='قیمت')
    discount = models.IntegerField(null=True, blank=True, verbose_name='تخفیف')
    category = models.ManyToManyField(Category, related_name='categorys')
    description = models.TextField(max_length=1000, verbose_name='توضیحات')
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    photo = models.ImageField(upload_to='images/', verbose_name='عکس')
    user = models.ManyToManyField(User,  related_name='shop_book', blank=True, null=True)

    def __str__(self):
        return self.bookName


class comment(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    book_key = models.ForeignKey(Books, related_name='book_key', on_delete=models.CASCADE)
    text = models.TextField(max_length=700)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.book_key.bookName


class comment_form(ModelForm):
    class Meta:
        model = comment
        fields = ['text']
