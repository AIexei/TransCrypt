from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    return render(request, 'functionality/index.html')


def calculations(request):
    context = None
    html = render_to_string('functionality/_results.html', context)
    return HttpResponse(html)