from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# dogs = [
#     {'name': 'Chewy', 'breed': 'Korean Jindo', 'age': 6},
#     {'name': 'Daisy', 'breed': 'Sheltie/Australian Shepherd', 'age': 6},
#     {'name': 'Kylo', 'breed': 'Mini Australian Shepherd', 'age': 5},
# ]

from .models import Dog


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/details.html', {
        'dog': dog
    })

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    # success_url = '/dogs/{dog_id}'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'age']
    # success_url = '/dogs/{dog_id}'

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs'