from django.shortcuts import render, get_object_or_404, redirect
from .models import Link


# Create your views here.
def index(request):
	links = Link.objects.all()
	context = {
		"links": links
	}
	return render(request, 'links/index.html', context)

# oursite.com/google -> www.google.com
# shortened url -> longer final destination

def root_link(request, link_slug):
	link = get_object_or_404(Link, slug=link_slug)
	link.click() # This will increament the clicked field
	return redirect(link.url)

def add_link(request):
	print(request.POST)
	return render(request, 'links/create.html')