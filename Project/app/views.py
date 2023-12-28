from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Posts, Comments, Image
from .forms import ImageForm

class ListPosts(ListView):
    model = Posts

def index(request):
    posts = Posts.objects.all().prefetch_related('comment')
    coms = Comments.objects.all().select_related('user')
    return render(request, 'app/posts_list.html', context={'object_list': posts, 'coms': coms})

def imageView(request):
    if request.method == 'POST':
        form = ImageForm(data=request.POST, files=request.FILES)
        # print(request.POST.get('image'))
        if form.is_valid():
            print(form.cleaned_data['title'])
            form.save()
            return redirect('image')
    form = ImageForm()
    images = Image.objects.all()
    return render(request, 'app/form.html', context={'form': form, 'images': images})