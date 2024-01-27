from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import Form



def submit_form(request):
    return render(request, 'index.html')






def home(request):
    if request.method == 'POST':
        print(request.POST)
        
        form_ = dict(request.POST)
        del form_["csrfmiddlewaretoken"]
        form = dict(map(lambda x: (x[0], x[1][0]), form_.items()))
        print(form)
        Form.objects.create(
            **form
        )

    context = {'advantages': models.Our_advantages.objects.all().order_by('order'), 'students':models.Student.objects.all(), 'gallerys':models.Gallery.objects.all()
               ,'our_results':models.our_results.objects.all(),}
    return render(request, 'index.html', context)
    

def project(request):
    return render(request,'project.html')


def blog(request):
    return render(request,'blog.html')
