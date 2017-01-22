from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    tab=Post.objects.all()
    return render(request, 'blog/post_list.html', {'p': tab})
