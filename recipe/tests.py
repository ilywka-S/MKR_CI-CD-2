from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

# Create your tests here.
class RecipeViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        
        for i in range(12):
            Recipe.objects.create(
                title=f"Test Recipe {i}",
                description="Test description",
                instructions="Test instructions",
                ingredients="Test ingredients",
                category=self.category
            )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        
        self.assertIn('recipes', response.context)
        self.assertLessEqual(len(response.context['recipes']), 10)

    def test_category_detail_view(self):
        response = self.client.get(reverse('category_detail', args=[self.category.id]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        
        self.assertEqual(response.context['category'], self.category)