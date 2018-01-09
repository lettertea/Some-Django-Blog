from .models import Blog
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {
        'posts': Blog.objects.all().order_by("-posted")
    })


def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })


def contact(request):
    return render(request, 'contact.html')
