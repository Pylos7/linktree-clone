from django.shortcuts import render
from django.views.generic import ListView

from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
	# query for all the links link.object.all()
	# context={'link': links}
	# return render(request, 'link_list.html', context)
	
	model = Link
	# template called model_list.html -> link_list.html
 