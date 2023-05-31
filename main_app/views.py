from django.shortcuts import render
from .models import Sneaker
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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
  return render(request, 'sneakers/detail.html', {
    'sneaker': sneaker
  })

class SneakerCreate(CreateView):
  model = Sneaker
  fields = '__all__'

class SneakerUpdate(UpdateView):
  model = Sneaker
  fields = '__all__'

class SneakerDelete(DeleteView):
  model = Sneaker
  success_url = '/sneakers'