from django.shortcuts import render, redirect
from .models import Sneaker
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WornForm


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
  # instantiate the worn form to be rendered in detail.html
  worn_form = WornForm()
  return render(request, 'sneakers/detail.html', {
    'sneaker': sneaker, 'worn_form': worn_form
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
