from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from django.views.generic import(
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from main import models

class Index(View):
    def get(self,request):
        return HttpResponse("GET request")

    def post(self,request):
        return HttpResponse("POST request")

class CollegeDetail(DetailView):
    model = models.College
    template_name ='college_detail.html'

class Collegelist(ListView):
    model=models.College
    template_name='collegelist.html'
    context_object_name='colleges'

class CollegeCreate(CreateView):
    model=models.College
    template_name='collegecreate.html'
    fields='__all__'
    success_url='/college'

class StudentCreate(CreateView):
    model=models.Student
    template_name='studentcreate.html'
    fields='__all__'
    success_url='/'


class CollegeUpdate(UpdateView):
    model = models.College
    template_name = 'collegecreate.html'
    fields='__all__'
    success_url='/college'



class StudentDelete(DeleteView):
    model = models.Student
    template_name = "confirm.html"
    success_url='/'
