from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
    return render(request, 'myblog/post_list.html', {'posts': posts})
