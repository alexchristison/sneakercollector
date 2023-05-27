from django.shortcuts import render

# Baby step - usually a Model is used 
sneakers = [
  {'name': 'Air Jordan IV', 'brand': 'Nike', 'description': 'blue and white', 'year': 1989},
  {'name': 'Air Tech Challenge 2', 'brand': 'Nike', 'description': 'Aka - Air Agassi. Hot Lava. ', 'year': 1990},
]
# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def sneakers_index(request):
  return render(request, 'sneakers/index.html', {
    'sneakers': sneakers
  }) # see comment related in urls.py re: index vs sneakers_index