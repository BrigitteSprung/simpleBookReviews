from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Review

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "review_list.html", context)


# Need to set up a CRUD

# Retrieve
def review_detail(request, id):
    review = Review.objects.get(id=id)
    context = {
        "review": review
    }
    return render(request, "review_detail.html", context)

def review_create(request):
    return HttpResponse("Create a review")


def review_update(request, id):
    review = Review.objects.get(id=id)
    context = {
        "review": review
    }
    return render(request, "review_update.html", context)


def review_delete(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return redirect('/')