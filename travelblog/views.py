from django.shortcuts import render, redirect
from django.contrib import messages  # for displaying messages to users
from .models import Blog, UserProfile
from .forms import SignInForm

def write_blog(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        rating = request.POST.get('rating')
        username = request.POST.get('username')
        blog_text = request.POST.get('blog')
        print(f"This is {destination}")
        print(f"This is {rating}")
        print(f"This is {username}")
        print(f"This is {blog_text}")


        # Validate data
        if not all([destination, rating, username, blog_text]):
            messages.error(request, 'All fields are required')

            print('data validated')
            return redirect('blog')  # Redirect back to the blog page with an error message

        try:
            rating = float(rating)
        except ValueError:
            messages.error(request, 'Invalid rating')
            return redirect('blog')
        
        print('data added to db')
        new_blog = Blog(destination=destination, rate=rating, user=username, blog_content=blog_text)
        new_blog.save()

        messages.success(request, 'Blog posted successfully!')
        return redirect('blog')

    return render(request, 'blog.html')

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # Here, you should hash the password using Django's authentication system
            # For simplicity, I'm using set_password method assuming your model has a password field
            user_profile = UserProfile.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user_profile.set_password(form.cleaned_data['password'])
            user_profile.save()

            messages.success(request, 'Account created successfully. Please sign in.')
            return redirect('signin')  # Redirect to the sign-in page
    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})

def home(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_detail.html', {'blog': blog})
