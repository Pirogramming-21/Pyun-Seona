from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import *
from .forms import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def main(request):
    sort = request.GET.get('sort', '등록순')
    
    if sort == '찜하기순':
        posts = Post.objects.annotate(num_stars=Count('ideastar')).order_by('-num_stars')
    elif sort == '이름순':
        posts = Post.objects.order_by('title')
    elif sort == '등록순':
        posts = Post.objects.order_by('id')
    elif sort == '최신순':
        posts = Post.objects.order_by('-id')
    else:
        posts = Post.objects.all()
    
    return render(request, 'posts/list.html', {'posts': posts, 'sort': sort})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('idea:main')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detail.html', {'post': post})

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('idea:detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update.html', {'form': form, 'pk': pk})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('idea:main')

# devtool 관련 views
def add_devtool(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('idea:devtool_list')
    else:
        form = DevToolForm()
    return render(request, 'posts/add_devtool.html', {'form': form})

def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'posts/devtool_list.html', {'devtools': devtools})

# 여기서부터 추가
def detail_devtool(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    related_posts = Post.objects.filter(devtool=devtool.name)
    return render(request, 'posts/devtool_detail.html', {'devtool': devtool, 'related_posts': related_posts})

def update_devtool(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('idea:detail_devtool', pk=devtool.pk)
    else:
        form = DevToolForm(instance=devtool)
    return render(request, 'posts/edit_devtool.html', {'form': form, 'devtool': devtool})

def delete_devtool(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        devtool.delete()
        return redirect('idea:devtool_list')
    return render(request, 'posts/confirm_delete_devtool.html', {'devtool': devtool})

from django.http import JsonResponse


def change_interest(request):
    post_id = request.POST.get('post_id')
    action = request.POST.get('action')
    post = get_object_or_404(Post, id=post_id)

    if action == 'increase' and post.interest < 10:
        post.interest += 1
    elif action == 'decrease' and post.interest > 1:
        post.interest -= 1

    post.save()
    return JsonResponse({'interest': post.interest})

def toggle_star(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if IdeaStar.objects.filter(post=post, user=user).exists():
        IdeaStar.objects.get(post=post, user=user).delete()
        starred = False
    else:
        IdeaStar.objects.create(post=post, user=user)
        starred = True

    return JsonResponse({'starred': starred, 'count': post.ideastar_set.count()})

