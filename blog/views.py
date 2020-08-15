from django.shortcuts import render
from .models import Post

posts = [
	{

		'author': 'Isha Sharma',
		'title': 'Blog Post 1',
		'content': 'First post',
		'date_posted': 'April 10, 2020'
	},
	{

		'author': 'Ashutosh Sharma',
		'title': 'Blog Post 2',
		'content': 'GRE post',
		'date_posted': 'August 10, 2020'
	}
]

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})



# Create your views here.
