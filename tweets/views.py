from django.shortcuts import render
from .models import Tweet
# Create your views here.

def home(request):
    context = {
        'tweets' : Tweet.objects.all().order_by('-creation_date')[0:5]
    }
    return render(request, 'tweets/index.html', context=context)
