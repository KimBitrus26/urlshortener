import random, string

from django.shortcuts import render
from django.shortcuts import render

from .models import ShortenURL
from .forms import CreateShortURLForm


def home(request):
    return render(request, 'home.html')

def redirectView(request, url):
    current_obj = ShortenURL.objects.filter(shorten_url=url)
    if len(current_obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'obj':current_obj[0]}
    return render(request, 'redirect.html', context)

def createShortenURLView(request):
    if request.method == 'POST':
        form = CreateShortURLForm(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_characters_list = list(string.ascii_letters)
            random_characters=''
            for i in range(6):
                random_characters += random.choice(random_characters_list)
            while len(ShortenURL.objects.filter(shorten_url=random_characters)) != 0:
                for i in range(6):
                    random_characters += random.choice(random_characters_list)
            shorten_data = ShortenURL(original_url=original_website, shorten_url=random_characters)
            shorten_data.save()
            context = {}
            context["chars"] = random_characters
            context["shorten_data"] = shorten_data
            return render(request, 'urlcreated.html', context)
    
    else:
        form=CreateShortURLForm()
        context={'form': form}
        return render(request, 'create.html', context)
