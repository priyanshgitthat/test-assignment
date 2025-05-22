from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    @classmethod
    def create_default_categories(cls):
        default_categories = ['Mental Health', 'Heart Disease', 'Covid19', 'Immunization']
        for name in default_categories:
            cls.objects.get_or_create(name=name)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Links to Doctor
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def truncated_summary(self):
        words = self.summary.split()[:15]
        return ' '.join(words) + ('...' if len(self.summary.split()) > 15 else '')