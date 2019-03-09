from django.shortcuts import render
from .models import Articles

def home(request):
    data = {
        'title': 'Blog of beldmian',
        'news': Articles.objects.all()
    }
    return render(request,'blog/home.html', data)
def contact(request):
    return render(request, 'blog/contact.html', {'title' :'Contacts'})
