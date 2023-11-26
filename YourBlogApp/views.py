from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def Home(response):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, response))