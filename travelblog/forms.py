from django import forms
from .models import Blog
from .models import TravelReview


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('user', 'title', 'destination', 'rate', 'blog_content')

class TravelReviewForm(forms.ModelForm):
    class Meta:
        model = TravelReview
        fields = '__all__'

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['stars']

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
