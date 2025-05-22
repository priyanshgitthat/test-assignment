from django.shortcuts import render, redirect
from .models import BlogPost, Category
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

@login_required
def create_blog(request):
    if request.user.user_type != 'doctor':
        return redirect('patient_dashboard')
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('doctor_blogs')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog.html', {'form': form})

@login_required
def doctor_blogs(request):
    if request.user.user_type != 'doctor':
        return redirect('patient_dashboard')
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'doctor_blogs.html', {'posts': posts})

def patient_blog_list(request):
    category_id = request.GET.get('category')
    
    # Get all published posts ordered by newest first
    posts = BlogPost.objects.filter(status='published').order_by('-created_at')
    categories = Category.objects.all()
    
    # Filter by category if one is selected
    if category_id and category_id.isdigit():
        posts = posts.filter(category_id=int(category_id))
    
    return render(request, 'patient_blog_list.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': int(category_id) if category_id and category_id.isdigit() else None
    })