from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models


def home(request):
    context = {'advantages': models.Our_advantages.objects.all().order_by('order')}
    return render(request, 'index.html', context)