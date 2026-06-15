from django.shortcuts import render

from heroes_app.models import Programs, Stories,Gallery


# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def programs(request):
    our_programs = Programs.objects.all()
    context = {'our_programs': our_programs}
    return render(request, 'programs.html', context)
def gallery(request):
    our_photos = Gallery.objects.all()
    context = {'our_photos': our_photos}
    return render(request, 'gallery.html', context)
def stories(request):
    our_stories = Stories.objects.all()
    context = {'our_stories': our_stories}
    return render(request, 'stories.html', context)
def story_detail(request, story_id):
    story = Stories.objects.get(id=story_id)
    context = {'story': story}
    return render(request, 'story_detail.html', context)
