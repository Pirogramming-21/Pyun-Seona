from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post, Comment

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

@require_POST
def create_post(request):
    image = request.FILES.get('image')
    caption = request.POST.get('caption')
    post = Post.objects.create(user=request.user, image=image, caption=caption)
    return JsonResponse({
        'post_id': post.id,
        'image_url': post.image.url,
        'caption': post.caption
    })
    
def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return JsonResponse({'liked': liked, 'likes_count': post.likes.count()})

@require_POST
def add_comment(request):
    post_id = request.POST.get('post_id')
    text = request.POST.get('text')
    post = get_object_or_404(Post, id=post_id)
    
    comment = Comment.objects.create(user=request.user, post=post, text=text)
    
    return JsonResponse({
        'comment_id': comment.id,
        'user': comment.user.username,
        'text': comment.text,
        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
    })

@require_POST
def delete_comment(request):
    comment_id = request.POST.get('comment_id')
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    comment.delete()
    
    return JsonResponse({'success': True})