from django import forms
from .models import BlogPost, Category  # Add Category to imports

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'status']
        widgets = {
            'status': forms.RadioSelect(choices=BlogPost.STATUS_CHOICES),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['summary'].widget = forms.Textarea(attrs={'rows': 3})