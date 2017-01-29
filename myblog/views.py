from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.shortcuts import redirect


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
    return render(request, 'myblog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.yazar = request.user
            post.yayinlanma_tarihi = timezone.now()
            post.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, 'myblog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.yazar = request.user
            post.yayinlanma_tarihi = timezone.now()
            post.save()
            return redirect('/post/'+pk, pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myblog/post_edit.html', {'form': form})
