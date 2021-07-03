from django.shortcuts import render
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