from django.shortcuts import render

# Create your views here.

def frontPage(request):
   return render(request, 'core/base.html') 
