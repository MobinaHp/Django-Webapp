from django.urls import path
from .views import home, blog, write_blog, sign_in, blog_detail

urlpatterns = [
    path('home/', home, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:id>/', blog_detail, name='blog_detail'),
    path('write_blog/', write_blog, name='write_blog'),
    path('signin/', sign_in, name='signin'),
    path('', home, name='home'),  # This is a catch-all or default pattern, placed at the end.
]
