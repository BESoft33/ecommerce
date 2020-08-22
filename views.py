from django.shortcuts import render
from .models import Brand, Category, Item,User

# Create your views here.

def signup(request):

    return render(request,'signup.html')

def login(request):

    return render(request,'login.html')

def describe(request):
	user = User.objects.all()#Should display user by unique user id

	context = {
		'user':user,
	}

    return render(request,'describe.html',{'user':user})

def commerce(request):
	brands = Brand.objects.all()
	categories = Category.objects.all()
	items = Item.objects.all()
	user = User.objects.all()#Should display user by unique user id

	context = {
		'brands':brands,
		'categories':categories,
		'item':items,
		'user':user
	}
	return render(request,'commerce.html',context)

def home(request):
	user = User.objects.all()#Should display user by unique user id

	context = {
		'user':user
	}

	return render(request,'commerce.html',{'user':user})
