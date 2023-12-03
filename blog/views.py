from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Model

# Create your views here.


class Home(ListView):
    model = Model
    template_name = 'home.html'

class Detail(DetailView):
    model = Model
    template_name = 'detail.html'

class Create(CreateView):
    model = Model
    template_name = 'create.html'
    fields = ['FirstName', 'LastName', 'MiddleName', 'UserName', 'Email', 'Password']

class Update(UpdateView):
    model = Model
    template_name = 'update.html'
    fields = ['FirstName', 'LastName', 'MiddleName', 'UserName', 'Email', 'Password']

class Delete(DeleteView):
    model = Model
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    
    

