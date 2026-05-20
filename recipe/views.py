from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category

def main(request):
    recipes = Recipe.objects.order_by('?')[:10]
    return render(request, 'main.html', {'recipes': recipes})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    return render(request, 'category_detail.html', {'category': category})