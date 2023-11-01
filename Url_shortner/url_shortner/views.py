from django.shortcuts import render, redirect
from .models import *
import uuid

# def redirect_to_long_url(request, short_url):
#     try:
#         print(5)
#         shortened_url = urlshortner.objects.get(short_url=short_url)
#         return redirect(shortened_url.long_url)
#     except urlshortner.DoesNotExist:
#         return redirect("not_found_url")


# Create your views here.

def finder(request, pk):
     url_details = urlshortner.objects.get(short_url = pk)
     return redirect('https://' + url_details.long_url)

def home(request):
    if request.method == 'POST':

        data = request.POST

        long_url = data.get('long_url')
        # short_url = data.get('short_url')
        uid = str(uuid.uuid4())[:5]
        new_url = urlshortner(long_url = long_url, short_url = uid)
        new_url.save() 

        return redirect('/') 

    queryset = urlshortner.objects.all()

    context = {'urls':queryset}
    return render(request, 'home.html',context)
