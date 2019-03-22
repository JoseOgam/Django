from django.shortcuts import render
from .admin import Post


# Create your views here.

def post_view(request):
    obj = Post.objects.all()

    context = {
        'object': obj
    }

    return render(request, "post.html", context)
