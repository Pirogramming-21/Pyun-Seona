from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from .models import *

def review_list(request):
    reviews = Review.objects.all()
    context ={
        "reviews" : reviews,
    }
    return render(request, 'review_list.html', {'reviews': reviews})

def add_review(request):
    if request.method == "POST":
        Review.objects.create(
            title=request.POST["title"],
            year_release=request.POST["year_release"],
            genre=request.POST["genre"],
            scope=request.POST["scope"],
            running_time=request.POST["running_time"],
            content=request.POST["content"],
            director=request.POST["director"],
            actor=request.POST["actor"],
        )
        return redirect('review_list') 
    return render(request, 'review_write.html')


def review_detail(request, id):
    review = get_object_or_404(Review, id=id)
    
    previous_review = Review.objects.filter(id__lt=id).order_by('-id').first()
    next_review = Review.objects.filter(id__gt=id).order_by('id').first()
    
    context = {
        'review': review,
        'previous_review': previous_review,
        'next_review': next_review
    }
    return render(request, 'review_detail.html', context)

def review_update(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', id=review.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review_update.html', {'form': form})

def review_delete(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == "POST":
        review.delete()
    return redirect('review_list')