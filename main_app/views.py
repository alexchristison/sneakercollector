from django.shortcuts import render, redirect
from .models import Sneaker, Sock
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WornForm
from django.views.generic import ListView, DetailView



# Baby step - usually a Model is used 
# sneakers = [
#   {'name': 'Air Jordan IV', 'brand': 'Nike', 'description': 'blue and white', 'year': 1989},
#   {'name': 'Air Tech Challenge 2', 'brand': 'Nike', 'description': 'Aka - Air Agassi. Hot Lava. ', 'year': 1990},
#   {'name': 'Polly Shoes', 'brand': 'Zacks', 'description': 'Fugly', 'year': 1822 },
# 
# ]
# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def sneakers_index(request):
  sneakers = Sneaker.objects.all()
  return render(request, 'sneakers/index.html', {
    'sneakers': sneakers
  }) # see comment related in urls.py re: index vs sneakers_index

def sneakers_detail(request, sneaker_id):
  sneaker = Sneaker.objects.get(id=sneaker_id)
  # First, create a list of sock ids that the shoe does have
  id_list = sneaker.socks.all().values_list('id')
  # Query for the socks that the sneaker does not have by using the exclude method vs the filter method
  socks_sneaker_doesnt_have = Sock.objects.exclude(id__in=id_list)
  # instantiate the worn form to be rendered in detail.html
  worn_form = WornForm()
  return render(request, 'sneakers/detail.html', {
    'sneaker': sneaker, 'worn_form': worn_form, 'socks' : socks_sneaker_doesnt_have
  })

class SneakerCreate(CreateView):
  model = Sneaker
  fields = ['name', 'brand', 'description', 'year']

class SneakerUpdate(UpdateView):
  model = Sneaker
  fields = '__all__'

class SneakerDelete(DeleteView):
  model = Sneaker
  success_url = '/sneakers'

def add_worn(request, sneaker_id):
  # create a ModelForm instance using the data in request.POST
  form = WornForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_worn = form.save(commit=False)
    new_worn.sneaker_id = sneaker_id
    new_worn.save()
  return redirect('detail', sneaker_id=sneaker_id)

class SockList(ListView):
  model = Sock

class SockDetail(DetailView):
  model = Sock

class SockCreate(CreateView):
  model = Sock
  fields = '__all__'

class SockUpdate(UpdateView):
  model = Sock
  fields = ['name', 'color']

class SockDelete(DeleteView):
  model = Sock
  success_url = '/socks'

def assoc_sock(request, sneaker_id, sock_id):
  Sneaker.objects.get(id=sneaker_id).socks.add(sock_id)
  return redirect('detail', sneaker_id=sneaker_id)

def unassoc_sock(request, sneaker_id, sock_id):
  Sneaker.objects.get(id=sneaker_id).socks.remove(sock_id)
  return redirect('detail', sneaker_id=sneaker_id)
